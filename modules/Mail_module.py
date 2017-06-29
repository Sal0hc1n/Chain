'''
Mail_module.py
@author: Nicholas Sollazzo
@mail: sollsharp@gmail.com
@version: 0.3
@date: 23/06/17
@status: TBT
'''

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from modules.utils.pyJson import pyJson


class Mail(object):
    """docstring for Mail."""

    def __init__(self, chain):
        self.flag = chain
        self.cond = False
        self.act = True

    def send(self, from_gmail, from_gmail_psw, to_email, subject, body):  # TODO: implement

        # body = self.jsn.get('body')
        # html_path = self.jsn.get('html_path')
        # placeholder = self.jsn.get('placeholder')
        # link = self.jsn.get('link')

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
