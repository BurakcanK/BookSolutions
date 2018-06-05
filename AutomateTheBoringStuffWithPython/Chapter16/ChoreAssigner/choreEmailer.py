""" Random Chore Assignment Emailer

Takes a list of people's email addresses and a list of chores that need to be done and randomly
assigns chores to people. Emails each person the assigned chore.
"""

import random
import smtplib
import sys

chores = ['dishes', 'bathroom', 'vacuum', 'walk dog']
emails = ['example1@gmail.com', 'example2@gmail.com', 'example3@gmail.com',
          'example4@gmail.com']

assignedChores = dict()

# assing the chores
for i in range(len(chores)):
    randomEmail = random.choice(emails)
    randomChore = random.choice(chores)
    assignedChores[randomEmail] = randomChore

    # remove not to double assign
    chores.remove(randomChore)
    emails.remove(randomEmail)

# create an SMTP object
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)

# greet the SMTP server
smtpObj.ehlo()

# start tls encryption
smtpObj.starttls()

# login phase
emailFrom, password = input("Email: "), input("Password: ")
smtpObj.login(emailFrom, password)

for email, chore in assignedChores.items():
    print(chore, "is assigned to", email)
    smtpObj.sendmail(emailFrom, email,
                     'Subject: Assigned Chores\nHi, this week\'s job for you --> ' + chore)

# disconnect from the server
smtpObj.quit()
