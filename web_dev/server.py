from flask import Flask, render_template, url_for

app = Flask(__name__)


# export FLASK_APP=server.py
# export FLASK_ENV=development
# flask run


@app.route("/")
def hello_world():
    print(url_for('static', filename='favicon.ico'))  # /static/favicon.ico
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/blog")
def blog():
    return "these are my thoughts"


@app.route("/blog/2020/dogs")
def blog2():
    return "these is my dog"
