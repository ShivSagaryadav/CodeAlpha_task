def chatbot():
    print("Hi! I'm CodeAlpha Bot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input or "hi" in user_input:
            print("Bot: Hello there! How can I help you?")
        elif "name" in user_input:
            print("Bot: I'm CodeAlpha Chatbot!")
        elif "how are you" in user_input:
            print("Bot: I'm doing great, thanks for asking!")
        elif "bye" in user_input:
            print("Bot: Goodbye! Have a nice day.")
            break
        else:
            print("Bot: Sorry, I didn't understand that. Can you rephrase?")

chatbot()