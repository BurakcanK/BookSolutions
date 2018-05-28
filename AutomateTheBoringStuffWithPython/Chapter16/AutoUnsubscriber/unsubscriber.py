""" Auto Unsubscriber

Scans through your emails, finds the unsubscribe links in all your emails, and automatically
opens them in a browser. Uses IMAP server.
"""

import email
import imaplib
import webbrowser

from bs4 import BeautifulSoup

# get user info
email_, password = input("Email: "), input("Password: ")

# connect to gmail's imap server and login, auto logout with 'with' statement
with imaplib.IMAP4_SSL(host='imap.gmail.com') as mail:
    mail.login(email_, password)

    # select the inbox
    mail.select(mailbox='INBOX', readonly=True)

    # search the mailbox, iterate over all of the emails
    result, data = mail.search(None, 'ALL')

    for d in data[0].split():
        result1, data1 = mail.fetch(d, '(RFC822)')
        rawEmail = data1[0][1]

        # # create a BytesParser object and parse the rawEmail
        # parser = email.parser.BytesParser()
        # msg = parser.parsebytes(rawEmail)

        # shortcut for above
        msg = email.message_from_bytes(rawEmail)

        # a message object can be message/multipart or message/text
        # handle this situation
        parts = []
        if msg.get_content_maintype() == 'multipart':
            for part in msg.get_payload():
                if part.get_content_maintype() == 'text':
                    parts.append(part.get_payload(decode=True))
        elif msg.get_content_maintype() == 'text':
            parts.append(msg.get_payload(decode=True))

        parts = ''.join(str(part) for part in parts)

        # start looking for unsubscribe anchor
        soup = BeautifulSoup(parts, 'html.parser')

        for tag in soup.find_all('a'):
            if tag.text.lower() == 'unsubscribe':
                url = tag.get('href')
                webbrowser.open(url)
