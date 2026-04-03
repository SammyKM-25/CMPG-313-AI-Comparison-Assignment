import random 
def get_llm_response(user_input): 
    responses = { 
        "hello": "Hello! How can I assist you today?", 
        "my name is": "Nice to meet you! How can I help?", 
        "stressed": "I understand stress can be difficult. Would you like to talk about what's bothering you?", 
        "tired": "Getting enough rest is important. What's affecting your sleep schedule?", 
        "exam": "Exams can be challenging. Have you tried creating a study schedule?", 
    } 
    user_lower = user_input.lower() 
    for key, response in responses.items(): 
        if key in user_lower: 
            return response 
    return f"I hear you saying: '{user_input}'. Could you tell me more about that?" 
if __name__ == "__main__": 
    print("Modern LLM Chatbot (Simulated)") 
    print("Type 'quit' to stop.\n") 
    while True: 
        user = input("You: ") 
        if user.lower() == "quit": 
            print("Bot: Goodbye!") 
            break 
        print(f"Bot: {get_llm_response(user)}") 
