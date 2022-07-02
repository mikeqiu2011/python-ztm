from flask import Flask, render_template, url_for

app = Flask(__name__)


# export FLASK_APP=server.py
# export FLASK_ENV=development
# flask run


@app.route("/")
def hello_my_home():
    return render_template('index.html')


@app.route('/works.html')
def work():
    return render_template('works.html')


@app.route("/about.html")
def about():
    return render_template('about.html')


@app.route("/contact.html")
def contact():
    return render_template('contact.html')


@app.route("/components.html")
def components():
    return render_template('components.html')
