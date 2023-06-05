import torch
import re
from RewardFunction import reward1, reward2, reward3, reward2_cot, reward3_cot
import time
import difflib
from transformers import GenerationConfig


def clean_code(code):
    lines = code.split('\n')
    indented_code = []
    for line in lines:
        if line.strip().startswith(('def solution():', 'solution()')):
            indented_code.append(line.strip())
            continue

        # Replace underscores with underscores
        line = line.replace('\\', '')

        # Add indentation
        line = ' ' * 2 + line

        indented_code.append(line)

    return '\n'.join(indented_code)



class Reward:
    def __init__(self, model, tokenizer, batch_size, device, prompt_large, prompt_small, max_len = 1400):
        self.model = model
        self.tokenizer = tokenizer
        self.batch_size = batch_size
        self.device = device
        self.prompt_small = prompt_small
        self.prompt_large = prompt_large
        self. max_len = max_len
        self.model.eval()

    
    def extract_questions(self, text):
        # Define the regular expression pattern for questions
        pattern = r"(?:^|\s)[\w\s\d\W]+?\?"

        # Find all matches of the pattern in the text
        matches = re.findall(pattern, text)

        # Filter out any non-question matches
        questions = [match.strip() for match in matches if '?' in match]

        return questions
        
    def extract_comments(self, code_string):
        pattern = r"#.*"  # Regular expression pattern to match comments
        comments = re.findall(pattern, code_string)
        combined_comment = ""
        for comment in comments:
            combined_comment += comment[1:]
        return combined_comment

    def step(self, reset, actions, questions, answers, dones_prev):
        with torch.no_grad():
            if(not reset):
                set_of_prompts = []
                for action in actions:
                    questions_extracted = self.extract_questions(action)
                    # print(questions_extracted)
                    if(len(questions_extracted)>2):
                        set_of_prompts.append(questions_extracted)
                    else:
                        set_of_prompts.append([])



            contexts = []
            for question in questions: 
                contexts.append((question.rsplit("?",1)[0]).rsplit('.', 1)[0])

            input = []
            for j in range(len(questions)):
                if(reset):
                    input.append([contexts[j], questions[j], []])
                else:
                    input.append([contexts[j], questions[j], set_of_prompts[j]])
            
            # breakpoint()
            dones, outputs, rewards = self.generate_env(input, answers, dones_prev)
            comments = []
            # for output in outputs:
            #     comments.append(self.extract_comments(output))
            
            return dones, outputs, rewards, comments
                    

    def generate_env(self, input, answers, dones_prev):
        p='''
        ### Input: If Friend P's rate is 15 percent faster than Friend Q's, how many kilometers will Friend P have walked when they pass each other? A) 21 B) 21.5 C)22 D)22.5 E)23?
         
        ### Response:
        Let us think step by step, first we need to find the speed of P and Q, then we can find the time they meet, then we can find the distance P has walked.
        Let the speed of Q be x km/hr
        Then the speed of P is 1.15x km/hr
        total distance = 43 km
        Then they will meet at t = 43/(1.15x + x) = 43/(2.15x) = 20/x
        Distance travelled by P = 1.15x * 20/x = 23 km
        Answer: E
        '''
        # breakpoint()
        # Get reward based on Subquestion
        rewards1 = reward1(input)
        # breakpoint()
        # Reward based on subanswers
        rewards2 = []

        # Generate sub_question and question answers
        outs = []
        for i in range(len(input)):
            prompts = []
            questions = []
            for j in range(len(input[i][2])):
                questions.append(input[i][0] + input[i][2][j])
                prompts.append("### Instruction: solve the following input question step by step. "+ p + "\n ### Input: "+input[i][0] + input[i][2][j] + "?\n ### Response: \n Let us think step by step")
            if(len(prompts)>0):
                out = self.generate(prompts)
                rewards2.append(reward2_cot(questions, out))
            else:
                out=[]
                rewards2.append(0)
            merged = ""
            for j in range(len(out)):
                merged += "\n ### Input: "+ input[i][0] + input[i][2][j] + "?\n ### Response: \n Let us think step by step" + out[j]

            outs.append("### Instruction: solve the following input question step by step. "+ p + merged + "\n ### Input: " + input[i][1] +"?\n ### Response: \n Let us think step by step")
        
            # print("######OUTS:",outs)
        # print("OUTS:", outs[0])
        # Generate Question answer
        # breakpoint()
        s= time.time()
        outputs = self.generate(outs)
        e = time.time()
        # print("OUTPUTS:", outputs[0])
        # print("TIME INSIDE ENVIRONMENT GENERATE: ", e-s)
        
        # Get final reward
        dones, rewards3 = reward3_cot(answers, outputs, dones_prev, rewards1, rewards2)

        final_reward = rewards3


        return dones, outputs, final_reward
    

    def generate(self, input_prompt):
        # breakpoint()
        generation_config = GenerationConfig(
            temperature=0.95,
            top_p = 0.18
        )

        input_ids = self.tokenizer(input_prompt, return_tensors="pt", padding=True, truncation = True, max_length = self.max_len).input_ids.to(self.device)
        outputs=self.model.generate(
        input_ids=input_ids,
        generation_config=generation_config,
        return_dict_in_generate=True,
        output_scores=True,
        max_new_tokens=256,
        )
        result =[]
        for i in range(len(outputs.sequences)):

            result.append(self.tokenizer.decode(outputs.sequences[i][input_ids[i].shape[0]:])) 
        # print(result)
        # result = self.remove_common_prefix(input_prompt, result)
        # print(result[0])
        # print("TIME TO GENERATE SECOND PASS: ", e-s)
        return result


    def remove_common_prefix(self, i_str1, i_str2):
        # breakpoint()
        r_str2=[]
        for i in range(len(i_str1)):
            str1=i_str1[i]
            str2=i_str2[i]
            str2 = self.remove_common_parts(str1, str2)
            # pattern = re.compile(re.escape(str1))
            # match = pattern.search(str2)
            # if(match):
            #     str2 = str2[match.end():]
            # pattern = re.compile(re.escape("solution()\n"))
            # match = pattern.search(str2)
            # if(match):
            #     str2 = str2[:match.end()]

            # pattern = re.compile(re.escape("question"))
            # match = pattern.search(str2)
            # if(match):
            #     str2 = str2[:match.end()-8]
            # str2 = clean_code(str2)
            r_str2.append(str2)
        return r_str2
    


    def remove_common_parts(self, string1, string2):
        # Remove spaces from the strings for comparison
        string1_no_spaces = string1.replace(" ", "")
        string2_no_spaces = string2.replace(" ", "")

        # Compute the differences between the strings
        diff = difflib.ndiff(string1_no_spaces, string2_no_spaces)

        # Collect the differing characters while preserving spaces
        result = []
        for item in diff:
            if item[0] == " ":
                result.append(" ")
            elif item[0] == "+":
                result.append(item[2])

        # Convert the result list to a string
        result_string = "".join(result)

        return result_string


    
    