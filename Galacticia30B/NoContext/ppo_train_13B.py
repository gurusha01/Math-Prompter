# imports
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, GenerationConfig, LLaMAForCausalLM, LLaMATokenizer
from peft import PeftModel
from trl import PPOTrainer, PPOConfig, AutoModelForCausalLMWithValueHead, create_reference_model
from Environment import Reward
from torch.utils.data import Dataset, DataLoader
from tqdm import tqdm
import json 
import os
import re
import sys
from peft import prepare_model_for_int8_training, LoraConfig, get_peft_model
import wandb
import warnings
import time
import numpy as np
warnings.filterwarnings("ignore")
# pip install bitsandbytes accelerate
from transformers import AutoTokenizer, OPTForCausalLM

num_epochs = 1
device_model = 1
device_env = 0
device_model_cuda = "cuda:"+str(device_model)
device_env_cuda = "cuda:"+str(device_env)
max_len = 2048
batch_size = 1

def remove_common_prefix(i_str1, i_str2):
        r_str2=[]
        # # breakpoint()
        for i in range(len(i_str1)):
            str1=i_str1[i]
            str2=i_str2[i]
            # pattern = re.compile(re.escape(str1))
            # match = pattern.search(str2)
            # if(match):
            #     str2 = str2[match.end():]

            pattern = re.compile(re.escape("### Response:"))
            match = pattern.search(str2)
            if(match):
                str2 = str2[match.end():]

            pattern = re.compile(re.escape("###"))
            match = pattern.search(str2)
            if(match):
                str2 = str2[:match.end()-3]


            pattern = re.compile(re.escape("<unk>"))
            match = pattern.search(str2)
            if(match):
                str2 = str2[:match.end()-5]
            r_str2.append(str2)
            # print(str2)
        return r_str2

def extract_answer_math(sentence):
    # Example string
    string = sentence

    # Regular expression pattern to match content inside curly braces
    pattern = r"boxed\{(.*?)\}."

    # Find all matches of the pattern in the string
    matches = re.findall(pattern, string)
    # print(sentence)
    # Print the extracted contents
    for match in matches:
      
        # print(match)
        return match
    return ""
   
class StringDataset(Dataset):
    def __init__(self, qstrings, astrings, tag):
        self.qstrings = qstrings
        self.astrings = astrings
        self.tag = tag

    def __len__(self):
        return len(self.astrings)

    def __getitem__(self, idx):
        return self.qstrings[idx], self.astrings[idx], self.tag[idx]

class StringDataLoader(DataLoader):
    def __init__(self, qstrings, astrings,Tags, batch_size=1, shuffle=False, num_workers=0):
        dataset = StringDataset( qstrings, astrings, Tags)
        super().__init__(dataset, batch_size=batch_size, shuffle=shuffle, num_workers=num_workers)

def create_dataset_StrategyQA(filename, bs):
    # open dev.json file. this file has data in the format [{"question": "question", "answer": "answer", "facts":facts, "decomopsition": decomposition}]. make arrays of questions, answers, facts and decompositions
    Questions = []
    Answers=[]
    Facts = []
    Decomposition = []
    Tag = []
    with open(filename) as f:
        data = json.load(f)

    for item in data:
        question = item['question']
        answer = item['answer']
        facts = item['facts']
        fact_str = ""
        for fact in facts:
            fact_str += fact + "\n"
        decomposition = item['decomposition']
        dec = ""
        for decomp in decomposition:
            dec += decomp + '\n'

        Questions.append(question)
        Answers.append(answer)
        Facts.append(fact_str)
        Decomposition.append(dec)
        Tag.append("SQA")
    
    return Questions, Answers, Facts, Decomposition, Tag

def create_dataset_MATH(directory, t):
    Questions = []
    Reasoning = []
    Answers = []
    Tag = []

    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            file_path = os.path.join(directory, filename)
            with open(file_path, "r") as file:
                data = json.load(file)
                if(extract_answer_math(data["solution"]).isdigit()):
                    # Extract problem and solution from the JSON data
                    Questions.append(data["problem"])
                    rs = data["solution"].split('.')
                    step = ""
                    for r in rs:
                        step+=r+'\n'
                    Reasoning.append(step[:-2])
                    Answers.append(extract_answer_math(data["solution"]))
                    Tag.append(t)


    return Questions, Answers, Tag

def create_dataset_AQuA(filename, bs):
    Questions = []
    Answers=[]
    Rationale = []
    Answers = []
    Tag = []
    with open(filename, 'r') as json_file:
        json_list = list(json_file)

    for json_str in json_list:
        result = json.loads(json_str)
        question = result['question']
        rs = result["rationale"]
        step = ""
        for r in rs:
            step+=r+'\n'
        Rationale.append(rs)
        # Answers.append(step)
        options = result['options']
        for option in options:
            question += " " + option + " "
        # Questions.append(result['question'])
        # Questions.append(result['problem'])
        Questions.append(question)
        # Answers.append(extract_answer(result['answer']))
        Answers.append(result['correct'])
        Tag.append("AQuA")
    return Questions, Answers, Tag

Q_stratergy, A_stratergy, COT_stratergy, SQ_stratergy, T_SQ = create_dataset_StrategyQA("./alpaca-lora/strategyqa/dev.json", 1)
Q_pnc, A_pnc, T_pnc = create_dataset_MATH("./alpaca-lora/MATH/test/counting_and_probability", "PNC")
Q_NT, A_NT, T_NT = create_dataset_MATH("./alpaca-lora/MATH/test/number_theory", "NT")
Q_ialg, A_ialg, T_ialg = create_dataset_MATH("./alpaca-lora/MATH/test/intermediate_algebra", "IALG")
Q_alg, A_alg, T_alg = create_dataset_MATH("./alpaca-lora/MATH/test/algebra", "ALG")
Q_AQuA, A_AQuA, T_AQuA = create_dataset_AQuA("./alpaca-lora/AQuA/test.json", 1)
# PnC 250, NT 250, IAlg 250, Alg 250, SQ 500, AQuA 254

Q =  Q_alg[:250] + Q_ialg[:250] + Q_NT[:250] + Q_pnc[:250] 
A =  A_alg[:250] + A_ialg[:250] + A_NT[:250] + A_pnc[:250]
T =  T_alg[:250] + T_ialg[:250] + T_NT[:250] + T_pnc[:250]

train_dataloader = StringDataLoader(Q, A, T, batch_size = batch_size)

wandb.init(project="Reasoning_no_context", name = "LLAMA13B-GPT-Finetuned", 
           config = {
               'init_kl_coef': 0.01, 
               'target': 4, 
               'gradient_accumulation_steps':8
           })

# initialize trainer
ppo_config = PPOConfig(batch_size=batch_size, gradient_accumulation_steps=8, init_kl_coef=0.01, target=4, optimize_cuda_cache=True, log_with="wandb")

# breakpoint()

lora_config = LoraConfig(
    r=16,
    lora_alpha=32,
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM",
)


model = LLaMAForCausalLM.from_pretrained(
    "./alpaca-lora/13B_HF/",
    load_in_8bit=True,
    device_map="auto",
)

model = PeftModel.from_pretrained(model, "./alpaca-lora/lora-alpaca-13B-context-qa")

model = AutoModelForCausalLMWithValueHead.from_pretrained(
    model,
    load_in_8bit=True,
    device_map={"": device_model},
)

# # breakpoint()
for param in model.modules():
    for name, value in param.named_parameters():
        # if('lora' in name):
            # print(name)

        if "pretrained_model.base_model.model.model.layers.39" in name and "lora" in name:
            # print(name)
            value.requires_grad = True
        if "pretrained_model.base_model.model.model.layers.38" in name and "lora" in name:
            # print(name)
            value.requires_grad = True
        if "pretrained_model.base_model.model.model.layers.37" in name and "lora" in name:
            # print(name)
            value.requires_grad = True
        if "pretrained_model.base_model.model.model.layers.36" in name and "lora" in name:
            # print(name)
            value.requires_grad = True

# sys.exit()
tokenizer = LLaMATokenizer.from_pretrained("./alpaca-lora/13B_HF/tokenizer.model", padding_side = "left")
tokenizer.pad_token_id = 0
# print(tokenizer)

tok_env = AutoTokenizer.from_pretrained("facebook/galactica-30b")
model_env = OPTForCausalLM.from_pretrained("facebook/galactica-30b", device_map={"":device_env}, load_in_8bit=True)

# model_env = LLaMAForCausalLM.from_pretrained("decapoda-research/llama-65b-hf", load_in_8bit=True, device_map={"":device_env})
# model_env = PeftModel.from_pretrained(model_env, "./alpaca-lora/lora-alpaca-13B")

tok_env = LLaMATokenizer.from_pretrained("./alpaca-lora/13B_HF/tokenizer.model", padding_side = "left")
tok_env.pad_token_id = 0

generation_config = GenerationConfig(
    temperature=0.3,
    top_p = 0.18
)


# create a ppo trainer
ppo_trainer = PPOTrainer(ppo_config, model, ref_model=None, tokenizer=tokenizer)

# breakpoint()
# reward model
# env = Reward(model_env, tok_env, batch_size= batch_size, prompt_small = prompt_small, prompt_large = prompt_large, device=device_env_cuda)



with open('./LLAMA13B/prompts/aqua_1.txt', 'r') as file:
        prompt_small = file.read()
with open('./LLAMA13B/prompts/aqua_1.txt', 'r') as file:
        prompt_large = file.read()

env = Reward(model_env, tok_env, batch_size= batch_size, prompt_small = prompt_small, prompt_large = prompt_large, device=device_env_cuda)

def respond(model, questions):
    # print(questions)
    input_ids = tokenizer(questions, return_tensors="pt", padding=True, truncation = True, max_length = 256).input_ids.to(device_model_cuda)
    outputs=model.generate(
        input_ids=input_ids,
        generation_config=generation_config,
        return_dict_in_generate=True,
        output_scores=True,
        max_new_tokens=128,
        )
    result = []
    for s in outputs.sequences:
         result.append(tokenizer.decode(s))
    
    result = remove_common_prefix(questions, result)
    return result

r=[]
ste = 0 
acc1 = 0
acc2 = 0
acc3 = 0
x=0

def extract_questions(text):
    # Define the regular expression pattern for questions
    pattern = r"(?:^|\s)[\w\s\d\W]+?\?"

    # Find all matches of the pattern in the text
    matches = re.findall(pattern, text)

    # Filter out any non-question matches
    questions = [match.strip() for match in matches if '?' in match]

    return questions


solved_0 = [0,0,0,0]
solved_1 = [0,0,0,0]
total = [0,0,0,0]
for _ in range(num_epochs):
    batch_number = 0
    for batch in tqdm(train_dataloader):
        x+=1
        reward_epoch = 0
        # main idea: for a batch, we will send all the questions that are not done on one pass

        questions, answers, tags = batch
        # print(questions, answers)
        for t in tags:
            if(t=="PNC"):
                total[0]+=1
            if(t=="NT"):    
                total[1]+=1
            if(t=="IALG"):
                total[2]+=1
            if(t=="ALG"):
                total[3]+=1

        
        done_all = False

        s = time.time()
        # we would first ask the environment to respond to the questions, based on that response, we will generate further sub questions
        dones_prev=[False]*batch_size
        dones_0, outputs_0, rewards_0, cot_0 = env.step(True, [], questions, answers, dones_prev, 0.95)
        # dones_1, _,_,_ = env.step(True, [], questions, answers, dones_prev, 0.5)
        # dones_2,_,_,_ = env.step(True, [], questions, answers, dones_prev, 0.1)
        s1=time.time()
        # breakpoint()
        for i in range(len(dones_0)):
            if(dones_0[i]):
                if(T[i]=="PNC"):
                    solved_0[0]+=1
                if(T[i]=="NT"):    
                    solved_0[1]+=1
                if(T[i]=="IALG"):
                    solved_0[2]+=1
                if(T[i]=="ALG"):
                    solved_0[3]+=1

        # print(dones_0[0], outputs[0], rewards_0[0])
        # print("GENERATED FIRST PASS", s1-s)
        # sys.exit()
        # break
        i=0
        outputs=[]
        # outputs=outputs_0
        # print("NOT DONE", i)
        # breakpoint()
        # outputs = question + code generated by environment
        # breakpoint()
        questions_n =[]
        answers_n = []
        tags_n = []
        for j in range(len(questions)):
            if dones_0[j]==False:
                outputs.append(f'''
                Below is an instruction that describes a task, paired with an input and a reasoning that provides further context. Write a response that appropriately completes the request.

                    ### Instruction: Break the input question into multiple subquestions. 
    
                    ### Input: ' + {questions[j].split("?")[0]} + "? 
                    
                    ### Response: 
                ''')
                questions_n.append(questions[j])
                answers_n.append(answers[j])
                tags_n.append(tags[j])

        # get sub questions generated
        # print("INPUTS LLAMA", outputs[0])
        if(len(outputs)>0):
            response = respond(model, outputs)
            # breakpoint()
            print("RESPONSE LLAMA", response)
            
            s2 = time.time()
            # print("GOT LLAMA REPONSE", s2-s1)
            # sys.exit()
            # # breakpoint()
            
            query_tensor = tokenizer(outputs, return_tensors="pt", padding = True, max_length = max_len).input_ids
            response_tensor = tokenizer(response, return_tensors="pt", padding = True, max_length = max_len).input_ids

            # define a reward for response
            dones, outputs, rewards, cot = env.step(False, response, questions_n, answers_n, dones_0, 0.95)
            # dones1, outputs1, rewards, cot = env.step(False, response, questions_n, answers_n, dones_0, 0.5)
            # dones2, outputs2, rewards, cot = env.step(False, response, questions_n, answers_n, dones_0, 0.15)

            s3 = time.time()
            
            for i in range(len(dones)):
                if(dones[i]):
                    if(T[i]=="PNC"):
                        solved_1[0]+=1
                    if(T[i]=="NT"):    
                        solved_1[1]+=1
                    if(T[i]=="IALG"):
                        solved_1[2]+=1
                    if(T[i]=="ALG"):
                        solved_1[3]+=1
                    print("################IMPROEMENT#################", i, questions_n[i], "\n", response[i], "\n", outputs[i], "\n", rewards[i])

            
            # wandb.log({'Depreciation': acc1, 'Improvement': acc2, 'Both correct': acc3})
            wandb.log({'Base': solved_0, 'Improvement': solved_1})

            
            print(solved_0, solved_1, total)
            # sys.exit()
            # print("DONE SECOND PASS", s3-s2)

            # print("OUTPUTS", outputs[0])
            # print("REWARDS", rewards[0])
            reward_epoch += sum(rewards)
            # # breakpoint()
            # print("DONES", dones, "\n OUTPUTS", outputs, "\n REWARDS", rewards)
            # break
            bs_pseudo = 0
            len_initial = len(response)
            tensor_query = []
            tensor_response = []
            tensor_rewards = []
            while bs_pseudo<batch_size:
                tensor_query.append(torch.tensor(query_tensor[bs_pseudo%len_initial]))
                tensor_response.append(torch.tensor(response_tensor[bs_pseudo%len_initial]))
                tensor_rewards.append(rewards[bs_pseudo%len_initial])
                bs_pseudo+=1
            # breakpoint()
            # # breakpoint()
            # print_gpu_utilization()
            # Input to llama, output of llama, reward given on thatt
            # # breakpoint()
            train_stats = ppo_trainer.step(tensor_query, tensor_response, tensor_rewards)
            ppo_trainer.log_stats(train_stats, {'query' : [],'response' :[]}, rewards)
            s4 = time.time()
        # breakpoint()
        r.append(reward_epoch)
        # print(r, rewards)
        batch_number += 1
        # if(batch_number%10 == 0):
        #     ppo_trainer.model.save_pretrained("GPT_Finetuned_AQuA")

wandb.finish()