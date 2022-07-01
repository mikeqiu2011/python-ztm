from flask import Flask, render_template

app = Flask(__name__)


# export FLASK_APP=server.py
# export FLASK_ENV=development
# flask run


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/blog")
def blog():
    return "these are my thoughts"


@app.route("/blog/2020/dogs")
def blog2():
    return "these is my dog"
