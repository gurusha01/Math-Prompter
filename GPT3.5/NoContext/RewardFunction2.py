import torch
import nltk
import signal
from io import StringIO
import re 
import spacy
import time
from sklearn.metrics.pairwise import cosine_similarity
import textwrap

nlp = spacy.load('en_core_web_sm')

import sys
import contextlib

@contextlib.contextmanager
def redirect_stdout(target):
    original = sys.stdout
    try:
        sys.stdout = target
        yield
    finally:
        sys.stdout = original

def handler(signum, frame):
    raise Exception("Timeout!")

def evaluate_code(code, final, answer, done_prev):
        # breakpoint()
        code = code.strip()
        # print(code)
        runtime_error = False
        infinite_loop = False
        if(final):
            reward = 0 
        else:
            reward = -1

        try:
            
            # code = clean_code(code)
            # print("$$$",code)
            compiled_code = compile(code, '<string>', 'exec')
            if(final):
                stdout = StringIO()
                with redirect_stdout(stdout):
                    exec(code)
                out = stdout.getvalue()
                if(int(out.strip()) == int(answer.strip())):
                    print("OUTPUT MATCHES ANSWER", out.strip(), answer.strip())
                    reward = reward + 1

        except Exception as e:
            infinite_loop=True
        finally:
            signal.alarm(0)
       
        if(not final and not runtime_error and not infinite_loop):
            reward = 0.25
            
        if(final and done_prev and reward==0):
            reward=-1

        return reward 
    
def extract_code(code_unclear):
    code_unclear = code_unclear.strip()
    pattern = re.compile(re.escape("solution()\n"))
    match = pattern.search(code_unclear)
    if(match):
        code_unclear = code_unclear[:match.end()]
    return code_unclear

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

def reward1(input):
    reward = []
    for i in range(len(input)):
        question = input[i][1]
        sub_question = input[i][2]
        nouns_question = get_nouns([question])
        nouns_sub_question = get_nouns(sub_question)
        difference = 1 - len(nouns_question.symmetric_difference(nouns_sub_question))/len(nouns_question)
        reward.append(torch.tensor(difference))
    return reward

def reward2(outputs):
    reward=0
    for code_unclear in outputs:
        code = extract_code(code_unclear)
        reward += evaluate_code(code, False, 0, False)
    return reward

def reward3(answers, outputs, dones_prev, reward1, reward2):
    reward=[]
    dones = []
    for i in range(len(answers)):
        r = evaluate_code(outputs[i], True, answers[i], dones_prev[i])
        reward.append(r + reward1[i] + reward2[i])
        if(r>0):
            dones.append(True)
        else:
            dones.append(0)
    return dones, reward

def get_nouns(sentence):
    nouns = []
    for s in sentence:
        tagged_words = nltk.pos_tag(nltk.word_tokenize(s))
        for word, pos in tagged_words:
            if pos.startswith('NN'):
                nouns.append(word)
    return set(nouns)

'''
def reward2(questions, outputs):
    s = time.time()
    r=torch.tensor(0.0)
    for i in range(len(questions)):
        # Get the word embeddings for each sentence
        embedding1 = nlp(questions[i]).vector
        embedding2 = nlp(outputs[i]).vector

        # Calculate the cosine similarity between the embeddings
        similarity_score = cosine_similarity([embedding1], [embedding2])[0][0]
        r+= torch.tensor(10.0*similarity_score)
    e = time.time()
    # print("TIME FOR REWARD 2", e-s)
    return r


def reward3(answers, outputs, outputs_0, reward1, reward2):
    reward=[]
    dones = []
    s = time.time()
    for i in range(len(answers)):
        outputs = find_answer(outputs)
        outputs_0 = find_answer(outputs_0)
        if(outputs[i].strip() == answers[i].strip()):
            print("REWARD +100")
            r = torch.tensor(100.0)
        elif(outputs_0[i].strip() == answers[i].strip()):
            print("REWARD -100")
            r = torch.tensor(-100.0)
        else:
            r= torch.tensor(0.0)
        reward.append(r + reward1[i] + reward2[i])
        if(r>0):
            dones.append(True)
        else:
            dones.append(0)
    e = time.time()
    # print("TIME FOR REWARD 3", e-s)
    return dones, reward
'''

def find_answer(outputs):
    answers = []
    for output in outputs:
        pattern = re.compile(re.escape("Answer:"))
        match = pattern.search(output)
        if(match):
            output = output[match.end():]
        answers.append(output)
    return answers