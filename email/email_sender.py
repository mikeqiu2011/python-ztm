import smtplib
from email.message import EmailMessage
import os
from string import Template
from pathlib import Path

username = os.getenv('USER')
password = os.getenv('PASSWORD')

email = EmailMessage()
email['from'] = 'mike qiu'
email['to'] = 'mikeqiu2011@163.com'
email['subject'] = 'how are you'

html = Template(Path('index.html').read_text())
email.set_content(html.substitute({'name': 'tintin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(username, password)
    smtp.send(email)
    print('all good boss')
