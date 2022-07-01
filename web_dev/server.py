from flask import Flask

app = Flask(__name__)


# export FLASK_APP=server.py
# export FLASK_ENV=development
# flask run


@app.route("/")
def hello_world():
    return "<p>Hello, mike!</p>"


@app.route("/blog")
def blog():
    return "these are my thoughts"
