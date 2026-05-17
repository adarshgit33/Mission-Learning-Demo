# Rule based AI Chat bot

import datetime
import time

name=input("Enter your name : ")
currenthour=datetime.datetime.now().hour

if 5<=currenthour<11:
    print("good morning -" ,name)
elif 11<=currenthour<16:
    print("good afternoon -" ,name)
elif 16<=currenthour<21:
    print("good evening -" ,name)
else:
    print(" Bhut Raat ho gayi hai -",name)

print("Welcome , aapka Swagat hai \n")
print("You can ask me basic questions and say Bye if you want to exit ----")

responses ={
    "hello" : "Hi Adarsh how are you , how can I help you ? ",
    "how are you" : "I am very fine , thank you." ,
    "who are you" : "I am smart AI chat bot" ,
    "motivate me" : "Keep going , every bug of your code will make you a better developer"
}

#Function
def userquestion(questions) :
    questions=questions.lower()
    for eachkey in responses :
        if eachkey in questions:
            return responses[eachkey]
    return "I am not sure about your question , I am still learning"

# loop for the repetative task
while True:

    userinput = input("\nEnter your question :")
    reply = userquestion(userinput)
    print("AI chat bot response :" ,reply)

    if "bye" in userinput.lower():
        break
    