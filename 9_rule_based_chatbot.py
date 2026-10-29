while True:
    msg = input("You: ").lower()

    if "hello" in msg or "hi" in msg:
        print("Bot: Hello! How can I help ?")
    elif "name" in msg:
        print("Bot: I am a simple chatbot.")
    elif "course" in msg:
        print("Bot: Computer Engineering")
    elif "bye" in msg or "exit" in msg:
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: Sorry! I don't understand.")