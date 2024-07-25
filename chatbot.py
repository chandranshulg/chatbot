def get_response(user_input):
    responses = {
        "hi": "Hello!",
        "hello": "Hi there!",
        "how are you": "I'm just a program, so I don't have feelings, but thanks for asking!",
        "bye": "Goodbye! Have a nice day!",
        "what is your name": "I'm a simple chatbot created by you.",
        "what can you do": "I can chat with you and provide predefined responses. I'm constantly learning!",
        "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
        "what is the capital of India": "The capital of india is New Delhi.",
        "who is the president of the united states": "As of my last update, the president is Joe Biden.",
        "what is the weather today": "I can't provide real-time weather updates, but you can check a weather website or app!",
        "tell me a fun fact": "Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible!",
        "what is the square root of 16": "The square root of 16 is 4.",
        "who wrote 'hamlet'": "Hamlet was written by William Shakespeare.",
        "how old are you": "I'm as old as the code that created me, which was written recently!",
        "what is the meaning of life": "That's a deep question! Many believe it's to find happiness and purpose, but everyone has their own interpretation."
    }
    
    user_input = user_input.lower()
    
    if user_input in responses:
        return responses[user_input]
    
    # Check for partial matches or more complex responses
    if "your name" in user_input:
        return "I'm a simple chatbot created by you."
    if "capital" in user_input:
        return "Can you specify the country you're asking about?"
    if "president" in user_input:
        return "Can you specify the country you're asking about?"
    if "weather" in user_input:
        return "I can't provide real-time weather updates, but you can check a weather website or app!"
    if "joke" in user_input:
        return "Why don't scientists trust atoms? Because they make up everything!"
    if "fun fact" in user_input:
        return "Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible!"
    if "square root" in user_input:
        return "Can you specify the number you want to find the square root of?"
    if "who wrote" in user_input:
        return "That's an interesting question. Can you specify the work you're asking about?"

    return "Sorry, I don't understand that. Can you rephrase?"

def chat():
    print("Chatbot: Hi! How can I help you today?")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a nice day!")
            break
        
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()
