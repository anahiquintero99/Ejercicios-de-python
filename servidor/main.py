from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_word():
    return 'Hola Anahi, esfuerzate más.'

if __name__ == "__main__":
    app.run()