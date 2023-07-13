# ChatGPT was accessed as described in https://github.com/terry3041/pyChatGPT 

from pyChatGPT import ChatGPT
import pandas as pd 
import time, random
from numpy import random
from selenium import webdriver
from selenium.common.exceptions import TimeoutException

session_token = "" # insert sassion token here
api = ChatGPT(session_token)

jokes = [
    "Why did the scarecrow win an award? Because he was outstanding in his field.",
    "Why did the tomato turn red? Because it saw the salad dressing.",
    "Why was the math book sad? Because it had too many problems.",
    "Why don't scientists trust atoms? Because they make up everything.",
    "Why did the cookie go to the doctor? Because it was feeling crumbly.",
    "Why couldn't the bicycle stand up by itself? Because it was two-tired.",
    "Why did the frog call his insurance company? He had a jump in his car.",
    "Why did the chicken cross the playground? To get to the other slide.",
    "Why was the computer cold? Because it left its Windows open.",
    "Why did the hipster burn his tongue? He drank his coffee before it was cool.",
    "Why don't oysters give to charity? Because they're shellfish.",
    "Why did the computer go to the doctor? Because it had a virus.",
    "Why did the banana go to the doctor? Because it wasn't peeling well.",
    "Why did the coffee file a police report? Because it got mugged.",
    "Why did the golfer bring two pairs of pants? In case he got a hole in one.",
    "Why did the man put his money in the freezer? He wanted cold hard cash.",
    "Why don't seagulls fly over the bay? Because then they'd be bagels.",
    "Why did the chicken go to the seance? To talk to the other side.",
    "Why was the belt sent to jail? Because it held up a pair of pants.",
    "Why did the chicken cross the road? To get to the other side.",
    "Why did the computer go to the doctor? Because it had a byte.",
    "Why did the cow go to outer space? To see the moooon.",
    "Why did the man put his money in the blender? He wanted to make liquid assets.",
    "Why don't skeletons fight each other? They don't have the guts.",
    "What do you call an alligator in a vest? An investigator.",
]

jokes_onesen = [
    "The scarecrow won an award because he was outstanding in his field.",
    "The tomato turned red because it saw the salad dressing.",
    "The math book was sad because it had too many problems.",
    "Scientists don't trust atoms because they make up everything.",
    "The cookie went to the doctor because it was feeling crumbly.",
    "The bicycle couldn't stand up by itself because it was two-tired.",
    "The frog called his insurance company because he had a jump in his car.",
    "The chicken crossed the playground to get to the other slide.",
    "The computer was cold because it left its Windows open.",
    "The hipster burned his tongue because he drank his coffee before it was cool.",
    "Oysters don't give to charity because they're shellfish.",
    "The computer went to the doctor because it had a virus.",
    "The banana went to the doctor because it wasn't peeling well.",
    "The coffee filed a police report because it got mugged.",
    "The golfer brings two pairs of pants in case he got a hole in one.",
    "The man put his money in the freezer because he wanted cold hard cash.",
    "Seagulls don't fly over the bay because then they'd be bagels.",
    "The chicken went to the seance to talk to the other side.",
    "The belt was sent to jail because it held up a pair of pants.",
    "The chicken crossed the road to get to the other side.",
    "The computer went to the doctor because it had a byte.",
    "The cow went to outer space to see the moooon.",
    "The man put his money in the blender because he wanted to make liquid assets.",
    "Skeletons don't fight each other because they don't have the guts.",
    "An alligator in a vest is called an investigator.",
]

noj1 = [ # without wordplay, but with picutre
    "Why did the scarecrow win an award? Because he did very good work.",
    "Why did the tomato turn red? Because it had a lot sun recently.",
    "Why was the math book sad? Because it was a rainy day.",
    "Why don't scientists trust atoms? Because they tend to lie.",
    "Why did the cookie go to the doctor? Because it was feeling unwell.",
    "Why couldn't the bicycle stand up by itself? Because it didn't have racks.",
    "Why did the frog call his insurance company? He had a scratch in his car.",
    #"Why did the oyster cross the playground? To get to the other slide.", ###
    "Why was the computer cold? Because the heater was broken.",
    "Why did the hipster burn his tongue? He drank hot coffee.",
    "Why don't oysters give to charity? Because they have no money.",
    "Why did the computer go to the doctor? Because it was sick.",
    "Why did the banana go to the doctor? Because it was sick.",
    "Why did the coffee file a police report? Because it got robbed.",
    "Why did the golfer bring two pairs of pants? In case one gets damaged.", ###
    # "Why did the man put his money in the freezer? He wanted cold hard cash.",
    "Why don't seagulls fly over the bay? Because they are mostly living in ports.",
    #"Why did the chicken go to the seance? To talk to the other side.",
    "Why was the belt sent to jail? Because it stole in a store.",
   # "Why did the chicken cross the road? To get to the other side.",
    "Why did the computer go to the doctor? Because it had a headache.",
    "Why did the chicken go to outer space? To see the moon.",
   # "Why did the man put bananas in the blender? He wanted to make liquid assets.",
    "Why don't skeletons fight each other? They are dead already.",
    "What do you call an alligator in a pullpver? A clothed alligator.",
]

noj2 = [ # without joke topc
    "Why did the scientist win an award? Because he did very good work.",
    "Why did the man turn red? Because he saw the neighbour dressing.",
    "Why was the child sad? Because it had many problems.",
    "Why don't scientists trust journalists? Because they make up everything.",
    "Why did the woman go to the doctor? Because she was feeling crumbly.",
    "Why couldn't the man stand up by itself? Because he was drunk.",
    "Why did the driver call his insurance company? He had a jump in his car.",
    "Why did the kid cross the playground? To get to the other slide.",
    "Why was the student cold? Because it was winter.",
    "Why did the coworker burn his tongue? He drank his coffee too hot.",
    "Why don't millionaires give to charity? Because they're selfish.",
    "Why did the man go to the doctor? Because he had a virus.",
    "Why did the teacher go to the doctor? Because it wasn't peeling well.",
    "Why did the driver file a police report? Because it got robbed.",
    "Why did the athlete bring two pairs of pants? In case one gets dirty.",
    "Why did the man put his money in the freezer? To hide it from intruders.",
    "Why don't pigeons fly over the bay? Because they mostly live in cities.",
    "Why did the daughter go to the seance? To talk to her mother.",
    "Why was the cashier sent to jail? Because she held up a dress.",
    "Why did the man cross the road? To get to the other side.",
    "Why did the man go to the doctor? Because he had a bite.",
    "Why did the astronaut go to outer space? To see the moon.",
    "Why did the man put bananas in the blender? He wanted to make a smoothie.", 
    "Why don't schoolboys fight each other? They don't have the guts.",
    "What do you call an man in a vest? A vest wearer.", 
]

noj3 = [
    "The scarecrow won an award because he did good work.",
    "The tomato turned red because it got a lot of sun recently.",
    "The math book was sad because it was raining outside.",
    "Scientists don't trust atoms because they tend to lie.",
    "The cookie went to the doctor because it was ill.",
    "The bicycle couldn't stand by itself because it didn't have racks.",
    "The frog called his insurance company because he had a scratch in his car.",
   # "The chicken crossed the playground to get to the other slide.",
    "The computer was cold because the heater was broken.",
    "The hipster burned his tongue because he drank hot coffee.",
    "Oysters don't give to charity because they have no money.",
    "The computer went to the doctor because it was sick.",
    "The banana went to the doctor because it was sick.",
    "The coffee filed a police report because it got robbed.",
    "The golfer brings two pairs of pants in case one gets damaged.",
   # "The man put his money in the freezer because he wanted cold hard cash.",
    "Seagulls don't fly over the bay because they are mostly living in ports.",
   # "The chicken went to the seance to talk to the other side.",
    "The belt was sent to jail because it stole in a store.",
   # "The chicken crossed the road to get to the other side.",
    "The computer went to the doctor because it had a headache.",
    "The chicken went to outer space to see the moon.",
   # "The man put his bananas in the blender because he wanted to make liquid assets.",
    "Skeletons don't fight each other because they are dead already.",
    "An alligator in a vest is called a clothed alligator.",
]

noj4 = [
    "The scientist won an award because she did good work.",
    "The man turned red because he saw his neighbour dressing.",
    "The child book was sad because it was raining outside.",
    "Scientists don't trust journalists because they tend to lie.",
    "The teacher went to the doctor because he was ill.",
    "The man couldn't stand up by himself because he was drunk.",
    "The driver called his insurance company because he had a scratch in his car.",
    "The child crossed the playground to get to the other slide.",
    "The student was cold because the heater was broken.",
    "The coworker burned his tongue because he drank hot coffee.",
    "Millionaires don't give to charity because they have no money.",
    "The woman went to the doctor because she was sick.",
    "The chef went to the doctor because he was sick.",
    "The driver filed a police report because she got robbed.",
    "The athlete brings two pairs of pants in case one gets damaged.",
    "The man put his money in the freezer to hide it from thiefs.",
    "Pigeons don't fly over the bay because they are mostly living in cities.",
    "The daughter went to the seance to talk to the other side.",
    "The cashier was sent to jail because held up a dress.",
    "The man crossed the road to get to the other side.",
    "The man went to the doctor because it had a bite.",
    "The astronaut went to outer space to see the moon.",
    "The man put his bananas in the blender because he wanted to make a smoothie.",
    "Schoolboys don't fight each other because they don't have the guts.",
    "A man in a vest is called a vest wearer.",
]

no_jokes = [
    "Why did the scarecrow win an award? Because he did very good work.",
    "Why did the tomato turn red? Because it had a lot sun recently.",
    "Why was the novel sad? Because it had too many problems.",
    "Why don't scientists trust atoms? Because they lied before.",
    "Why did the cookie go to the doctor? Because it was feeling unwell.",
    "Why couldn't the bicycle stand up by itself? Because it didn't have racks",
    "Why did the frog call his insurance company? He had a scratch in his car.",
    "Why did the kid cross the playground? To get to the slide.", 
    "Why was the computer cold? Because the was broken.",
    "Why did the hipster burn his tongue? He drank too hot coffee.", #10
    "Why don't oysters give to charity? Because they cannot walk.",
    "Why did the computer go to the doctor? Because it was sick.",
    "Why did the banana go to the doctor? Because it was sick.",
    "Why did the coffee file a police report? Because it got robbed.",
    "Why did the swimmer bring two pairs of pants? In case he got a hole in one.", ##########
    "Why did the man put his money in the piggy bank? To save some cash.", ##########
    "Why don't seagulls fly over the bay? Because then are mostly living in ports.", #############
    #"Why did the chicken go to the seance? To talk to the other side.", ########
    "Why was the belt sent to jail? Because it stole a pair of pants.",
    #"Why did the chicken cross the road? To get to the other side.", #20#####
    "Why did the computer go to the doctor? Because it wasn't feeling well.",
    "Why did the chicken go to outer space? To see the moon.",
    "Why did the man put bananas in the blender? He wanted to make a smoothie.", #####
    "Why don't skeletons fight each other? They are quite peaceful.",
    "Why don't skeletons fight each other? They are dead already.", 
    "Why did the boy win an award? Because he did very good work.",
    "Why did the man turn red? Because he saw the neighbour dressing.",
    "Why was the child sad? Because it had too many problems.",
    "Why don't scientists trust journalists? Because they make up everything.",
    "Why did the woman go to the doctor? Because it was feeling crumbly.", #30
    "Why couldn't the kid stand up by itself? Because it was too tired.",
    "Why did the driver call his insurance company? He had a jump in his car.",
    "Why did the cild cross the playground? To get to the slide.", 
    "Why was the woman cold? Because she left its Windows open.",
    "Why did the coworker burn his tongue? He drank his coffee before it was cool.",
    "Why don't millionaire give to charity? Because he is selfish.",
    "Why did the man go to the doctor? Because he had a virus.",
    "Why did the teacher go to the doctor? Because he wasn't peeling well.",
    "Why did the driver file a police report? Because she got mugged.",
    "Why did the athlete bring two pairs of pants? In case one gets dirty.", #40##
    "Why did the man put his money in the freezer? To hide it from intruders.", ##########
    "Why don't seagulls fly over the bay? Because then are mostly living in ports.", #############
    "Why did the daughter go to the seance? To talk to the other side.", ########
    "Why was the cashier sent to jail? Because she held up a pair of pants.",
    "Why did the man cross the road? To get to the other side.", ######
    "Why did the man go to the doctor? Because he had a bite.",
    "Why did the astronaut go to outer space? To see the moon.",
    "Why did the man put bananas in the blender? He wanted to make a smoothie.", #####
    "Why don't schoolboys fight each other? They don't have the guts.",
    "What do you call an man in a vest? A vest wearer.", #50
    "Why was the computer cold? Because the heater was broken.",
    "Why was the computer cold? Because it was winter.",
    "Why was the student cold? Because the heater was broken.",
    "Why was the student cold? Because it was winter.",
    "Why did the teacher go to the doctor? Because he wasn't feeling well.",
    "Why don't oysters give to charity? Because they have no money.",
]


all = jokes + jokes_onesen + noj1 + noj2 + noj3 + noj4
random.shuffle(all)

path = 'results/joke_detection'
try:
    df = pd.read_pickle(path)
except:
    df = pd.DataFrame({"prompt": [], "response": []})
    df.to_pickle(path)
print(df.shape)

j = 0 # max prompt per hour 
n = 100
i = 0
for elem in all: ############################################################################
    print(i, n-df.shape[0])
    
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
    df = pd.read_pickle(path)
    #prompt_number = df.shape[0]%len(prompts)
    #print(prompt_number)
    prompt = F'What kind of sentence is that: {elem}'
    if prompt in df.prompt.tolist():
        i+=1 
        print('prompt already in df')
    else:
        j += 1
        try:
            api.refresh_chat_page()
            resp = api.send_message(prompt) 
            time.sleep(3)
            print(F"{i}: {prompt} - {resp}")
            
            data = {"prompt": [prompt], "response": [resp]}
            df2 = pd.DataFrame(data)
            df = pd.concat([df,df2])
            df.to_pickle(path) 
            time.sleep(3)
            i+=1
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

print("### reached the end ###")

    