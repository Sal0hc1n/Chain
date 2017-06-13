'''
Mail_module.py
@author: Nicholas Sollazzo
@mail: sollsharp@gmail.com
@version: 0.2
@date: 11/06/17
@status: TBT
'''

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from modules.base.module import Module
from utils.pyJson import pyJson


class Mail(Module):
    """docstring for Mail."""

    def __init__(self):
        self.path = 'data/modules_data/mail.json'
        self.jsn = pyJson(self.path)
        self.jsn.set({'module_name': 'Mail_module'})
        self.cond = False
        self.act = True

    def action(self, arg):
        switcher = {
            'send': send
        }
        funAction = switcher[arg]
        funAction()

    def send(self):  # TODO: implement
        from_gmail = self.jsn.get('from_gmail')
        from_gmail_psw = self.jsn.get('from_gmail_psw')
        to_email = self.jsn.get('to_email')
        subject = self.jsn.get('subject')
        body = self.jsn.get('body')
        html_path = self.jsn.get('html_path')
        placeholder = self.jsn.get('placeholder')
        link = self.jsn.get('link')

        # formattazzione messaggio
        mime_msg = MIMEMultipart('alternative')
        mime_msg['Subject'] = subject
        mime_msg['From'] = from_gmail
        mime_msg['To'] = to_email

        part1 = MIMEText(body, 'plain')
        mime_msg.attach(part1)

        if html_path is not None:  # TODO: controllare che funzioni
            with open(html_path, 'rb') as fp:
                html_part = fp.read()
            part2 = MIMEText(html_part, 'html')
            mime_msg.attach(part2)

        # invio mail con link
        s = smtplib.SMTP('smtp.gmail.com:587')
        s.starttls()
        s.login(from_gmail, from_gmail_psw)
        # s.sendmail(SendMail,ReciveMail,messaggio)
        if placeholder is not None and link is not None:  # TODO: controllare che funzioni
            s.sendmail(from_gmail, to_email,
                       mime_msg.as_string().replace(placeholder, link))
        else:
            s.sendmail(from_gmail, to_email, mime_msg.as_string())
        s.quit()

        if s:
            return True
        else:
            return False
