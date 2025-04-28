responses = {
    "hello": "Hi there!",
    "how are you": "I'm just a bot, but I'm doing great!",
    "bye": "Goodbye!"
}

while True:
    user_input = input("You: ").lower()
    if user_input == "exit":
        break
    print("Bot:", responses.get(user_input, "I don't understand."))
