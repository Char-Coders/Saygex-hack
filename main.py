
import flask
import flask_cors
from chatbot import Inference


chatbot = Inference()
chatbot_doc = Inference(True)
app = flask.Flask(__name__)
flask_cors.CORS(app)

@app.route('/', methods=['GET'])
def uwu():
    return 'Pani Peele Bhai'

@app.route('/reset')
def reset():
    chatbot = Inference()

@app.route('/chatUser')
def chatUser():
    text = flask.request.args['text']
    resp = chatbot_doc.run(text)
    return {'content': resp['content']}

@app.route('/chatDoctor')
def chatDoctor():
    text = flask.request.args['text']
    resp = chatbot.run(text)
    return {'content': resp['content']}

# def main():
#     while True:
#         ask = input("> ")
#         print(chat(ask))

if __name__ == "__main__":
    app.run()
