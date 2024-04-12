import asyncio
import flask
from chatbot import Inference


chatbot = Inference()

def chat(text):
    resp = chatbot.run(text)
    return resp
        
def main():
    while True:
        ask = input("> ")
        print(chat(ask))

if __name__ == "__main__":
    main()