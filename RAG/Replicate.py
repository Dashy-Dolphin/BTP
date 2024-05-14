import replicate


import subprocess, sys,os

command = ["export REPLICATE_API_TOKEN=r8_H4PU3ethewy9efNWEBl5r62j6OhzEXn0qsFYY", "echo $REPLICATE_API_TOKEN"]


subprocess.Popen(command[0], shell = True, executable="/bin/bash").wait()
subprocess.Popen(command[1], shell = True, executable="/bin/bash").wait()


#wait for subprocess to finish

queryfile  ="/home/sasi/Desktop/Final_Sem/CS4805_BTP/Exp2/entire_questions.txt"
contextfile="/home/sasi/Desktop/Final_Sem/CS4805_BTP/Exp2/entire_wiki_context.txt"
answerfile ="/home/sasi/Desktop/Final_Sem/CS4805_BTP/Exp2/entire_wiki_answers.txt"

with open(queryfile, 'r') as file:
    questions = file.readlines()

with open(contextfile, 'r') as file:
    contexts = file.readlines()


fp = open(answerfile, "w")


c1 ="Answer breifly with the help of the following context. "
# c1 = "Answer breifly."
for i in range(len(questions)):
    q = questions[i].replace("\n", "")
    c = contexts[i].replace("\n", "")
    
    fp.write("Question : " + q + "\n")
    fp.write("Context  : " + c + "\n")
    fp.flush()


    input_json = {
    "top_p": 0.9,
    "temperature": 0.75,
    "prompt": q,
    "system_prompt": c1 + c,
            "max_new_tokens": 500
    }
    
    ans = ""
    for event in replicate.stream(
        "meta/llama-2-13b-chat",
        input=input_json
    ):
        ans += str(event)
    ans =ans.replace("\n", "")
  
    fp.write("Answer   : " + ans + "\n")
    fp.write("\n\n ------------------- \n\n")
    fp.flush()

    print("Answered question " + str(i + 1))
    #strip the newline character
    #get input from the user
    # h=input()


fp.close()

     

