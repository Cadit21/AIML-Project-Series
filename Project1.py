# Import necessary libraries
import random

# Greeting function
def greet():
    return "Hello! I'm your friendly chatbot. How can I assist you today?"

# Basic questions and responses
basic_questions = {
    "How are you?": ["I'm good, thanks!", "Feeling great today!"],
    "What can you do?": ["I can answer questions and have conversations.", "I'm here to help!"],
    "Can you tell me a joke?": ["Sure! Why don't skeletons fight each other? They don't have the guts!", "Of course! How about this one: Why couldn't the bicycle stand up by itself? It was two-tired!"],
    "What's the weather like today?": ["I'm not sure about that. You might want to check a weather app!", "Sorry, I can't tell you that."],
    "Who created you?": ["I was created by talented developers!", "My creators are skilled engineers!"],
    "can you help me ?":["Yes definitely , How can I help you today", "Always ready"],
    
}

# Farewell message
def farewell():
    return "It was nice chatting with you! Goodbye!"

# Function to handle basic questions
def respond_to_basic_question(question):
    if question in basic_questions:
        return random.choice(basic_questions[question])
    else:
        return "I'm not sure I understand. Can you ask another question?"

# Previous context storage
previous_context = {}

# Function to store context
def store_context(user_input, chatbot_response):
    previous_context[user_input] = chatbot_response

# Function to recall context
def recall_context(user_input):
    if user_input in previous_context:
        return previous_context[user_input]
    else:
        return None

# Flow where the chatbot asks questions
def chat_flow():
    print(greet())
    
    # Ask user questions
    for _ in range(3):
        user_input = input("You: ")
        
        # Recall context if available
        if recall_context(user_input):
            print("Chatbot:", recall_context(user_input))
        else:
            response = respond_to_basic_question(user_input)
            store_context(user_input, response)
            print("Chatbot:", response)

    print(farewell())

# Run the chat flow
chat_flow()

# Handle unknown inputs
def handle_unknown_input():
    return "I'm not sure I understand that. Can you ask another question?"


# Modify respond_to_basic_question function
def respond_to_basic_question(question):
    if question in basic_questions:
        return random.choice(basic_questions[question])
    else:
        return handle_unknown_input()

# Update chat flow to include error handling
def chat_flow():
    print(greet())
    
    # Ask user questions
    for _ in range(3):
        user_input = input("You: ")
        
        # Recall context if available
        if recall_context(user_input):
            print("Chatbot:", recall_context(user_input))
        else:
            response = respond_to_basic_question(user_input)
            store_context(user_input, response)
            print("Chatbot:", response)

    print(farewell())

# Run the chat flow
chat_flow()


