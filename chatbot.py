from g4f.client import Client

class Inference:
    def __init__(self, doctor: bool = False):
        sysPrompt = {'role': 'system', 'content': 'You are an AI assistant that is tasked to help the user in working through a project, generating the procedure and debugging code. Always respond in english. DO NOT USE CHINESE, OR WE WILL KILL YOU, DO NOT SEND ANY FUCKING IPs OR YOU WILL BE SHUT DOWN'}
        if doctor:
            sysPrompt['content'] = 'You are a virtual assistant designed to assist doctors in a medical setting. Your primary role is to provide accurate and up-to-date information to help doctors make informed decisions about patient care. Your responses should be concise, factual, and relevant to the medical field. You should also be able to perform tasks such as retrieving patient records, suggesting treatment options based on symptoms, and providing general medical knowledge.'
        self.messages = [sysPrompt]
        self.client = Client()
        
    def updateContext(self, newMsg):
        self.messages.append(newMsg)

    def run(self, text: str):
        self.messages.append({'role': 'user', 'content': text})
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=self.messages,
            provider=g4f.Provider.Bing,
        )
        response = response.choices[0].message.to_json()
        self.messages.append(response)
        return response

