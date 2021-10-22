from flask import Flask, flash, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.post("/api/save_message")
def save_message():
    if request.method == 'POST':
        email = request.form['email']
        text = request.form['text']
        print(email, text)
    return "Ok"
