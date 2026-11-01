while True:
    msg = input("You: ").lower()

    if "hello" in msg or "hi" in msg:
        print("Bot: Hello! How can I help you?")

    elif "name" in msg:
        print("Bot: I am a simple Python chatbot.")

    elif "course" in msg:
        print("Bot: You are studying Computer Engineering.")

    elif "how are you" in msg:
        print("Bot: I am fine! Thank you.")

    elif "college" in msg:
        print("Bot: Welcome to our college chatbot!")

    elif "help" in msg:
        print("Bot: Sure! Ask me about your name, course or college.")

    elif "thank" in msg:
        print("Bot: You're welcome!")

    elif "bye" in msg or "exit" in msg:
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry! I don't understand. Please try again.")