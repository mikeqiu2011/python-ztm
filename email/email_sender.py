import smtplib
from email.message import EmailMessage
import os

username = os.getenv('USER')
password = os.getenv('PASSWORD')

email = EmailMessage()
email['from'] = 'mike qiu'
email['to'] = 'mikeqiu2011@163.com'
email['subject'] = 'how are you'

email.set_content('i am a Python master!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(username, password)
    smtp.send(email)
    print('all good boss')
