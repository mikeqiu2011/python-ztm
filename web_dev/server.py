from flask import Flask, render_template, request, redirect

app = Flask(__name__)


# export FLASK_APP=server.py
# export FLASK_ENV=development
# flask run


@app.route("/")
def hello_my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name=None):
    return render_template(page_name)


@app.post('/submit_form')
def login():
    data = request.form.to_dict()
    write_to_file(data)
    return redirect('thankyou.html')


def write_to_file(data):
    with open('db.csv', mode='a') as f:
        email = data['email']
        subject = data['subject']
        message = data['message']
        f.write(f'{email},{subject},{message}\n')
