'''
Mail_module.py
@author: Nicholas Sollazzo
@mail: sollsharp@gmail.com
@version: 1.1
@date: 01/07/17
@status: WRK
@note: html mail not implemented, but possible
'''
import getpass

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

    def send(self, args=None):

        html_path = None
        placeholder = None # for links
        link = None
        from_gmail = 'athome.hub01@gmail.com'
        from_gmail_psw = 'steins;gate'

        # body = self.jsn.get('body')
        # html_path = self.jsn.get('html_path')
        # placeholder = self.jsn.get('placeholder')
        # link = self.jsn.get('link')
        if args is not None:
            to_email = args[0]
            subject = args[1]
            body = args[2]

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
            s.ehlo()
            s.starttls()
            s.login(from_gmail, from_gmail_psw)

            if placeholder is not None and link is not None:  # TODO: controllare che funzioni
                s.sendmail(from_gmail, to_email,
                           mime_msg.as_string().replace(placeholder, link))
            else:
                s.sendmail(from_gmail, to_email, mime_msg.as_string())
            s.quit()

        else:
            print('=== EMAIL ===')
            to_email = input('reciver: ')
            subject = input('subject: ')
            body = input('body: ')

            return [to_email, subject, body]
