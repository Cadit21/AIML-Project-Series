class AdmissionChatbot:
    def __init__(self):
        self.admission_info = {
            "procedures": "To apply for admission, you need to submit an online application form.",
            "requirements": "The admission requirements include a high school diploma and standardized test scores (e.g., SAT, ACT).",
            "deadlines": "The application deadline for the upcoming semester is on July 15, 2024.",
            "programs": "We offer various undergraduate and graduate programs in different fields."
        }
        self.user_profile = {
            "name": None,
            "questions_asked": []
        }
    
    def greet_user(self):
        print("Welcome! I'm your College Admission Chatbot. How can I assist you today?")
    
    def respond_to_query(self, query):
        query = query.lower()
        response = None
        
        if "procedure" in query or "process" in query:
            response = self.admission_info["procedures"]
        elif "requirement" in query or "eligibility" in query:
            response = self.admission_info["requirements"]
        elif "deadline" in query or "due date" in query:
            response = self.admission_info["deadlines"]
        elif "program" in query or "courses" in query:
            response = self.admission_info["programs"]
        else:
            response = "I'm sorry, I don't have information about that. Please contact the admission office for further assistance."
        
        self.user_profile["questions_asked"].append(query)
        return response
    
    def chat(self):
        self.greet_user()
        while True:
            user_input = input("You: ").strip()
            
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print("Chatbot: Thank you for using the Admission Chatbot. Goodbye!")
                break
            
            response = self.respond_to_query(user_input)
            print("Chatbot:", response)
            
            # Update user profile or context based on the conversation
            if self.user_profile["name"] is None:
                self.update_user_profile(user_input)
    
    def update_user_profile(self, user_input):
        if "my name is" in user_input.lower():
            parts = user_input.split("my name is ")
            if len(parts) > 1:
                self.user_profile["name"] = parts[1]
                print("Chatbot: Nice to meet you, {}!".format(self.user_profile["name"]))

# Instantiate the AdmissionChatbot and start the conversation
if __name__ == "__main__":
    chatbot = AdmissionChatbot()
    chatbot.chat()
    
