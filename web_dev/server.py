from flask import Flask, render_template, url_for

app = Flask(__name__)


# export FLASK_APP=server.py
# export FLASK_ENV=development
# flask run


@app.route("/")
def hello_my_home():
    return render_template('index.html')


@app.route('/<string: page_name>')
def html_page(page_name=None):
    return render_template(page_name)
