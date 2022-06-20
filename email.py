# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 20:28:29 2022

@author: User
"""

import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Raisa Azad'
email['to'] = 'jahan047.israt@gmail.com'
email['subject'] = 'Tui ekta baal!!'
email.set_content('I just sent you this mail with python')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls() #tls is an encryption mechanism
    smtp.login('raizad007@gmail.com','EYAYINAS328')
    smtp.send_message(email)
    print('all good boss!')    