

def chatbot_response(user_input):

    user_input = user_input.lower().strip()

    if user_input == "hello" or user_input == "hi":
        return "Hi! How can I help you?"

    elif user_input == "how are you":
        return "I am fine, thanks! How about you?"

    elif user_input == "what is your name":
        return "I am a simple Python chatbot."

    elif user_input == "what can you do":
        return "I can chat with you using predefined replies."

    elif user_input == "thank you" or user_input == "thanks":
        return "You're welcome!"

    elif user_input == "bye" or user_input == "goodbye":
        return "Goodbye! Have a nice day!"

    else:
        return "Sorry, I don't understand that."


def main():

    print("================================")
    print("       WELCOME TO CHATBOT       ")
    print("================================")
    print("Type 'bye' to exit the chatbot.\n")

    while True:

        user_input = input("You: ")

        response = chatbot_response(user_input)

        print("Bot:", response)

        if user_input.lower().strip() in ["bye", "goodbye"]:
            break



if __name__ == "__main__":
    main()
