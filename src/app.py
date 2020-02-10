from flask import Flask

app = Flask(__name__)  # '__main__'

@app.route('/')
def hello():
    return "Gelllo"

if __name__ == '__main__':
    app.run(port=4995)