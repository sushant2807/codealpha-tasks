def chatbot():
    print("🤖 Chatbot: Hello! Welcome to my chatbot.")
    print("Type 'bye' to exit the chat.")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Chatbot: Hi!")

        elif user == "how are you":
            print("Chatbot: I'm fine, thanks!")

        elif user == "what is your name":
            print("Chatbot: I am a Python chatbot.")

        elif user == "who created you":
            print("Chatbot: I was created using Python.")

        elif user == "bye":
            print("Chatbot: Goodbye! Have a nice day!")
            break

        else:
            print("Chatbot: Sorry, I don't understand that.")


chatbot()