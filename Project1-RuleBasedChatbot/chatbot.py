print("welcome to the rule-based chatbot!")
print("how can i help you..?")

while True:
    user_input = input("you: ").strip().lower()
    
    if user_input in ["hi", "hello", "hey"]:
        print("chatbot: hi! thankyou for your message. How can i help you?")
        
    elif user_input in ["how are you", "how are you doing", "how are you"]:
        print("chatbot: Good. BTW i am a simple rule-based chatbot created to assist you..!")
        
    elif user_input in ["what's your name?", "who are you?", "what is your name"]:
        print("chatbot: my name is asad chatbot. i am a simple rule-based chatbot created to assist you..!")
        
    elif user_input in ["bye", "goodbye"]:
        print("chatbot: Goodbye! Have a great day!")
        break
        
    else:
        print("chatbot: I'm sorry, I don't understand that. Can you please rephrase?")
