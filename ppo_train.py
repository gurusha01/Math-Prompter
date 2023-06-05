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
warnings.filterwarnings("ignore")

num_epochs = 1
device_model = 1
device_env = 0

device_model_cuda = "cuda:1"
device_env_cuda = "cuda:0"

def is_numeric_string(input_string):
    return input_string.isdigit()

def extract_answer(sentence):
    TRUE_RE = re.compile(r"$\boxed{")
    match = TRUE_RE.search(sentence)
    if match:
        match_str = match.group(0).strip()
        match_str = match_str.replace("#### ", "")
        return match_str
    else:
        return -1

def extract_answer_math(sentence):
    # Example string
    string = sentence

    # Regular expression pattern to match content inside curly braces
    pattern = r"boxed\{(.*?)\}"

    # Find all matches of the pattern in the string
    matches = re.findall(pattern, string)
    # print(sentence)
    # Print the extracted contents
    for match in matches:
      
        # print(match)
        return match
    return ""
   
class StringDataset(Dataset):
    def __init__(self, qstrings, astrings):
        self.qstrings = qstrings
        self.astrings = astrings

    def __len__(self):
        return len(self.astrings)

    def __getitem__(self, idx):
        return self.qstrings[idx], self.astrings[idx]

class StringDataLoader(DataLoader):
    def __init__(self, qstrings, astrings, batch_size=1, shuffle=False, num_workers=0):
        dataset = StringDataset( qstrings, astrings)
        super().__init__(dataset, batch_size=batch_size, shuffle=shuffle, num_workers=num_workers)

def create_dataset(filename, bs):
    Questions = []
    Answers=[]
    with open(filename, 'r') as json_file:
        json_list = list(json_file)

    for json_str in json_list:
        result = json.loads(json_str)
        question = result['question']
        options = result['options']
        # for option in options:
        #     question += " " + option + " "
        # Questions.append(result['question'])
        # Questions.append(result['problem'])
        Questions.append(question)
        # Answers.append(extract_answer(result['answer']))
        # Answers.append(options[ord(result['correct'])-ord("A")][2:])
        Answers.append(extract_answer(result['correct']))
    # breakpoint()
    train_idx = int(1* len(Questions))
    val_idx = int(1*len(Questions))
    train_set = StringDataLoader(Questions[:train_idx], Answers[:train_idx], batch_size = bs)
    val_set = StringDataLoader(Questions[train_idx: val_idx], Answers[train_idx: val_idx], batch_size = bs)
    test_set = StringDataLoader(Questions[val_idx:], Answers[val_idx:], batch_size = bs)
    
    return train_set, val_set, test_set

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

def create_dataset_math(directory, bs):
    # Initialize empty lists for problems and solutions
    # # breakpoint()
    problems = []
    solutions = []

    # Iterate over each JSON file in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            file_path = os.path.join(directory, filename)
            
            # Read the JSON file
            with open(file_path, "r") as file:
                data = json.load(file)
                
                # Extract problem and solution from the JSON data
                problem = data["problem"]
                solution = extract_answer_math(data["solution"])
                
                # Append problem and solution to the respective lists
                if(is_numeric_string(solution)):
                    problems.append(problem)
                    solutions.append(solution)
    
    train_idx = int(1* len(problems))
    val_idx = int(1*len(problems))
    train_set = StringDataLoader(problems[:train_idx], solutions[:train_idx], batch_size = bs)
    val_set = StringDataLoader(problems[train_idx: val_idx], solutions[train_idx: val_idx], batch_size = bs)
    test_set = StringDataLoader(problems[val_idx:], solutions[val_idx:], batch_size = bs)
    # breakpoint()
    return train_set, val_set, test_set

# Hyperparameters
data_file_name = './AQuA/train.json'
max_len = 2048
batch_size = 8

# wandb.init(project="Reasoning_with_context", name = "Model1_prompt2", 
#            config = {
#                'init_kl_coef': 0.01, 
#                'target': 4, 
#                'gradient_accumulation_steps':8
#            })

# initialize trainer
ppo_config = PPOConfig(batch_size=batch_size, gradient_accumulation_steps=8, init_kl_coef=0.01, target=4, optimize_cuda_cache=True)

# Create datasets
train_dataloader, val_dataloader, test_dataloader = create_dataset(data_file_name, bs = batch_size)
# breakpoint()

lora_config = LoraConfig(
    r=16,
    lora_alpha=32,
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM",
)

# # load environment
model_env = LLaMAForCausalLM.from_pretrained("13B_HF/", load_in_8bit=True, device_map={"": device_env})
# model_env = LLaMAForCausalLM.from_pretrained("TheBloke/vicuna-13B-1.1-HF",  load_in_8bit=True,  device_map={"": device_env}, trust_remote_code=True)

tok_env = LLaMATokenizer.from_pretrained("13B_HF/tokenizer.model", padding_side = "left")
tok_env.pad_token_id = 0


for param in model_env.parameters():
    param.requires_grad = False

model = LLaMAForCausalLM.from_pretrained(
    "13B_HF/",
    load_in_8bit=True,
    device_map="auto",
)

model = PeftModel.from_pretrained(model, "./lora-alpaca-13B")

model = AutoModelForCausalLMWithValueHead.from_pretrained(
    model,
    load_in_8bit=True,
    device_map={"": device_model },
)

# # breakpoint()
for param in model.modules():
    for name, value in param.named_parameters():
        if "pretrained_model.base_model.model.model.layers.31" in name and "lora" in name:
            # print(name)
            value.requires_grad = True
        if "pretrained_model.base_model.model.model.layers.30" in name and "lora" in name:
            # print(name)
            value.requires_grad = True
        if "pretrained_model.base_model.model.model.layers.29" in name and "lora" in name:
            # print(name)
            value.requires_grad = True

# sys.exit()
tokenizer = LLaMATokenizer.from_pretrained("13B_HF/tokenizer.model", padding_side = "left")
tokenizer.pad_token_id = 0
# print(tokenizer)

generation_config = GenerationConfig(
    temperature=0.95,
    top_p = 0.18
)


# create a ppo trainer
ppo_trainer = PPOTrainer(ppo_config, model, ref_model=None, tokenizer=tokenizer)

with open('./prompts/prompt_1.txt', 'r') as file:
        prompt_small = file.read()
with open('./prompts/prompt2_1.txt', 'r') as file:
        prompt_large = file.read()

# reward model
env = Reward(model_env, tok_env, batch_size= batch_size, prompt_small = prompt_small, prompt_large = prompt_large, device=device_env_cuda)

def respond(model, questions):
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

for _ in range(num_epochs):
    batch_number = 0
    for batch in tqdm(train_dataloader):
        x+=1
        reward_epoch = 0
        # main idea: for a batch, we will send all the questions that are not done on one pass

        questions, answers = batch
        # print(questions, answers)

        
        done_all = False

        s = time.time()
        # we would first ask the environment to respond to the questions, based on that response, we will generate further sub questions
        dones_prev=[False]*batch_size
        dones_0, outputs_0, rewards_0, cot_0 = env.step(True, [], questions, answers, dones_prev)
        s1=time.time()
        # breakpoint()
        # print(dones_0[0], outputs[0], rewards_0[0])
        # print("GENERATED FIRST PASS", s1-s)
        # sys.exit()
        # break
        i=0
        outputs=[]
        for i in range(len(outputs_0)):
            outputs.append(outputs_0[i])
        # outputs=outputs_0
        # print("NOT DONE", i)
        # # breakpoint()
        # outputs = question + code generated by environment
        # # breakpoint()
        for j in range(len(questions)):
            outputs[j]='Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.\n ### Instruction: break following question into subquestions.  \n ### Input: ' + questions[j] + " \n ### Response: "
        # get sub questions generated
        # print("INPUTS LLAMA", outputs[0])
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
        dones, outputs, rewards, cot = env.step(False, response, questions, answers, dones_0)
        for i in range(batch_size):
            print("#############################\n",questions[i],"\n ### OUTPUTS 0 \n", outputs_0[i].strip(),"\n LLAMA RESPONSE \n",  response[i], "\n OUTPUTS \n", outputs[i].strip())
                
            if(dones_0[i] and dones[i]):     ## Case where both are solved i.e. no improvement
                # print("#############################\n",questions[i],"\n ### OUTPUTS 0 \n", outputs_0[i].strip(),"\n LLAMA RESPONSE \n",  response[i], "\n OUTPUTS \n", outputs[i].strip())
                acc3+=1
            if(not dones_0[i] and dones[i]):  ## Case where actual improvement
                print("##########   IMPROVEMENT   #############\n",questions[i],"\n ### OUTPUTS 0 \n", outputs_0[i].strip(),"\n LLAMA RESPONSE \n",  response[i], "\n OUTPUTS \n", outputs[i].strip())
                acc2+=1
            if(dones_0[i] and not dones[i]):  ## Case where depriciation
                ques_llama = extract_questions(response[i])
                if(len(ques_llama)>2):
                    print("##############   DEPRECIATION   ###############\n",questions[i],"\n ### OUTPUTS 0 \n", outputs_0[i].strip(),"\n LLAMA RESPONSE \n",  response[i], "\n OUTPUTS \n", outputs[i].strip())
                    acc1+=1
                else:
                    acc3+=1
        s3 = time.time()

        
        # wandb.log({'Depreciation': acc1, 'Improvement': acc2, 'Both correct': acc3})
        
        print(acc1, acc2, acc3)
        # sys.exit()
        # print("DONE SECOND PASS", s3-s2)

        # print("OUTPUTS", outputs[0])
        # print("REWARDS", rewards[0])
        reward_epoch += sum(rewards)
        # # breakpoint()
        # print("DONES", dones, "\n OUTPUTS", outputs, "\n REWARDS", rewards)
        # break
        tensor_query = [torch.tensor(lst) for lst in query_tensor]
        tensor_response = [torch.tensor(lst) for lst in response_tensor]
        # # breakpoint()
        # print_gpu_utilization()
        # Input to llama, output of llama, reward given on thatt
        # # breakpoint()
        train_stats = ppo_trainer.step(tensor_query, tensor_response, rewards)
        ppo_trainer.log_stats(train_stats, {'query' : [],'response' :[]}, rewards)
        s4 = time.time()

        # print("BACKPROP DONE", s4-s3)
        # print(train_stats)
        # print_gpu_utilization()
        # sys.exit()
        if(dones == len(questions)*[True] ):
            done_all = True
        i=i+1

        r.append(reward_epoch)
        # print(r, rewards)
        batch_number += 1
        if(batch_number%10 == 0):
            ppo_trainer.model.save_pretrained("checkpoint"+str(batch_number))

wandb.finish()