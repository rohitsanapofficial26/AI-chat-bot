import datetime
import time
presenthour=datetime.datetime.now().hour

name=input("Swagat hai aapka , Enter your name: ")

if 5<= presenthour <=11:
    print("Good Morning !! ")
elif 11<= presenthour <=17:
    print("Good afternoon !! ")
elif 17<= presenthour <=20:
    print("Good Evening !! ")
else:
    print("Soye nhii abhi tak soja yaar")

print("Welcome Namaste !! Welcome to our AI chatbot")
print("You can ask me basic  questtions, type Bye to exit from the bot")

# Its a chatbot memory who gives you the ans of your questions: 
responses={
    "hello": "hii ,How I can help you today ??",
    "how are you?":"I am fine and tell me what about you",
    "who are you":"I am your smart AI chatbot",
    "motivate me":"Keep going on!! Every mistake from your projects making you the better python developer",
    "happy":"Great to hear that",
    "funtions kya hota hai": "jakar videos dekho youtube parr!!"
}
def getresponsebot(user_question):
    user_question=user_question.lower()
    for eachkey in responses:
        if eachkey in user_question:
            return responses[eachkey]
        
    return "Abhii mujhe nahi aata I will learn. "

while True:
    userinput=input("Please ask your Question: ")
    reply=getresponsebot(userinput)
    print("Bot response: ",reply)
    
    if "bye" in userinput.lower():
        break