"""Controlling Your Computer Through Email

Check an email account every 15 minutes for any instructions about torrent and execute
those instructions automatically. Open magnet links with "BitTorrent".
"""

import email
import imaplib
import logging
import re
import smtplib
import subprocess
import time

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s %(message)s")

my_email = "your email"
to_email = "your email"
password = "your password"

while True:
    # connect to gmail's imap server and login, auto logout with "with" statement
    with imaplib.IMAP4_SSL("imap.gmail.com") as mail:
        mail.login(my_email, password)
        logging.debug("Connected to imap.gmail.com.")

        # select the inbox
        mail.select(mailbox="INBOX", readonly=True)

        # search the mailbox
        result, data = mail.search(None, "FROM " + my_email)

        # fetch the last email
        logging.debug("Fetching and parsing the last email..")
        result1, data1 = mail.fetch(data[0].split()[-1], "(RFC822)")
        raw_email = data1[0][1]

        # parse the email
        msg = email.message_from_bytes(raw_email)

        # a message object can be message/multipart or message/text
        # handle this situation
        parts = []
        if msg.get_content_maintype() == "multipart":
            for part in msg.get_payload():
                if part.get_content_maintype() == "text":
                    parts.append(part.get_payload(decode=True))
        elif msg.get_content_maintype() == "text":
            parts.append(msg.get_payload(decode=True))

        parts = "".join(str(part) for part in parts)

        # extract the magnet link, start qBitTorrent
        logging.debug("Extracting the magnet link from email..")
        magnet_link = re.search(r"magnet:?.*?(?=\\)", parts).group()
        subprocess.Popen(["qbittorrent", magnet_link])

        # create an SMTP object
        logging.debug("Getting ready to send feedback email..")
        smtp_pbj = smtplib.SMTP("smtp.gmail.com", 587)

        # greet the SMTP server
        smtp_pbj.ehlo()

        # start tls encryption
        smtp_pbj.starttls()

        # login phase
        smtp_pbj.login(my_email, password)

        # send feedback email
        smtp_pbj.sendmail(my_email, to_email,
                          "Subject: Torrent\nTorrent is being downloaded.")
        logging.debug("Feedback email is sent..\nLogging out from imap.")

    # wait 15 mins
    logging.debug("Waiting 15 mins..")
    time.sleep(60 * 15)
