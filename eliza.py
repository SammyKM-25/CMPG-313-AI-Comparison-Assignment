import re 
import random 
 
class CustomEliza: 
    def __init__(self): 
        self.rules = [ 
            (r"hello|hi|hey", ["Hello! How are you feeling today?", "Hi there! What's on your mind?"]), 
            (r"my name is (.+)", ["Nice to meet you, {0}. Tell me more.", "Hello {0}. How can I help?"]), 
            (r"i feel (stressed|anxious|worried)", ["Why do you feel {0}?", "What causes you to feel {0}?"]), 
            (r"i am tired|i feel tired", ["Why are you tired?", "Have you been sleeping well?"]), 
            (r"exam|test|study", ["Exams can be stressful. Tell me more.", "How are you preparing for your exams?"]), 
            (r"mother|father|parent", ["Tell me about your relationship with your {0}.", "How does that make you feel?"]), 
            (r".*", ["I see. Please tell me more.", "That's interesting. Can you elaborate?"]) 
        ] 
        self.compiled_rules = [(re.compile(p, re.IGNORECASE), r) for p, r in self.rules] 
    def respond(self, user_input): 
        for pattern, responses in self.compiled_rules: 
            match = pattern.match(user_input.strip()) 
            if match: 
                groups = match.groups() 
                response = random.choice(responses) 
                return response.format(*groups) if groups else response 
        return "Interesting. Please continue." 
 
eliza_chatbot = CustomEliza() 
def get_eliza_response(user_input): 
    return eliza_chatbot.respond(user_input) 
if __name__ == "__main__": 
    print("Custom ELIZA Chatbot") 
    print("Type 'quit' to stop.\n") 
    while True: 
        user = input("You: ") 
        if user.lower() == "quit": 
            print("ELIZA: Goodbye!") 
            break 
        print(f"ELIZA: {get_eliza_response(user)}") 
