def chatbot():
    print("Welcome to Basic Chatbot! Type something to begin.")
    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Bot: Hi!")
        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")
        elif user_input == "what's your name":
            print("Bot: I'm just a simple chatbot.")
        elif user_input == "what can you do":
            print("Bot: I can chat with you using simple rules!")
        elif user_input == "bye":
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: Sorry, I didn't understand that.")
