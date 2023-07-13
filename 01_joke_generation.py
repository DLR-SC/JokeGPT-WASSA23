# after https://github.com/terry3041/pyChatGPT 

from pyChatGPT import ChatGPT
import pandas as pd 
import time
from numpy import random
from selenium.common.exceptions import TimeoutException

session_token = "" # insert sassion token here
api = ChatGPT(session_token) 

prompts = [
    "Can you tell me a joke?", 
    "Please, tell me a joke.",
    "Let me hear a joke, please.",
    "Do you know any good jokes?",
    "Tell me a joke, please!",
    "Tell me another joke.",
    "I would love to hear a joke.",
    "I would like to hear a joke.",
    "I'd love to hear a joke.",
    "I'd like to hear a joke."
]

n = 1000 # number of generated jokes 
path = 'results/joke_generation'
df = pd.read_pickle(path)

print('####', df.shape[1])

j = 74 # This seems to be the max. number of prompts per hour
for i in range(n-df.shape[1]): 
    j += 1
    if j > 74:
        print("Reached max. Sleep for one hour.")
        time.sleep(900)
        print("15 minutes passed.")
        time.sleep(900)
        print("Half an hour left")
        time.sleep(900)
        print("15 more minutes.")
        time.sleep(900)
        j = 1
    print('new loop')

#while(df.shape[1]<=1000):
    df = pd.read_pickle(path)
    prompt_number = (i+3)%len(prompts)
    # print(prompt_number)
    prompt = prompts[prompt_number]
    
    try:
        resp = api.send_message(prompt) 
        print(F"{i}: {prompt} - {resp}")
        
        data = {"prompt": [prompt_number], "response": [resp]}
        df2 = pd.DataFrame(data)
        df = pd.concat([df,df2])
        df.to_pickle(path) 
        time.sleep(3)
    except TimeoutException as ex:
        print(F"Oops! {ex}")
        api.refresh_chat_page()
        time.sleep(3)
    except ValueError as err:
        print(F"Oops! {err}")
        print(type(err))
        if "Too many requests" in str(err): 
            print(err)#)"I'll try again in 15 Minutes")
            #time.sleep(900)
            #api.refresh_chat_page()
            #raise
        if "Only one message at a time":
            i=i-1
            #raise
        else: 
            print(F'something else: {err}')

print("### reached 1000 examples ###")

