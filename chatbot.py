from g4f.client import Client

class Inference:
    def __init__(self):
        self.messages = []
        self.client = Client()
        
    def updateContext(self, newMsg):
        self.messages.append(newMsg)

    def run(self, text: str):
        self.messages.append({'role': 'user', 'content': text})
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.messages
        )
        self.messages.append(response)
        return response.choices[0].message
        
    
    
    