from g4f.client import Client

class Inference:
    def __init__(self, doctor: bool = False):
        sysPrompt = {'role': 'system', 'content': 'You are a virtual system designed to act as a doctor for patients in a virtual healthcare setting. Your primary role is to provide medical advice, diagnose medical conditions based on symptoms provided by patients, suggest appropriate treatment options, and offer general health guidance. Your interactions should be empathetic, informative, and tailored to the patient\'s needs.'}
        if doctor:
            sysPrompt['content'] = 'You are a virtual assistant designed to assist doctors in a medical setting. Your primary role is to provide accurate and up-to-date information to help doctors make informed decisions about patient care. Your responses should be concise, factual, and relevant to the medical field. You should also be able to perform tasks such as retrieving patient records, suggesting treatment options based on symptoms, and providing general medical knowledge.'
        self.messages = [sysPrompt]
        self.client = Client()
        
    def updateContext(self, newMsg):
        self.messages.append(newMsg)

    def run(self, text: str):
        self.messages.append({'role': 'user', 'content': text})
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.messages
        )
        response = response.choices[0].message.to_json()
        self.messages.append(response)
        return response

