"""Random Chore Assignment Emailer

Take a list of people's email addresses and a list of chores that need to be done and randomly
assign chores to people. Email each person the assigned chore.
"""

import random
import smtplib

chores = ["dishes", "bathroom", "vacuum", "walk dog"]
emails = ["example1@gmail.com", "example2@gmail.com", "example3@gmail.com",
          "example4@gmail.com"]

assigned_chores = dict()

# assign the chores
for i in range(len(chores)):
    random_email = random.choice(emails)
    random_chore = random.choice(chores)
    assigned_chores[random_email] = random_chore

    # remove not to double assign
    chores.remove(random_chore)
    emails.remove(random_email)

# create an SMTP object
smtp_obj = smtplib.SMTP("smtp.gmail.com", 587)

# greet the SMTP server
smtp_obj.ehlo()

# start tls encryption
smtp_obj.starttls()

# login phase
email_from, password = input("Email: "), input("Password: ")
smtp_obj.login(email_from, password)

for email, chore in assigned_chores.items():
    print(chore, "is assigned to", email)
    smtp_obj.sendmail(email_from, email,
                     "Subject: Assigned Chores\nHi, this week's job for you --> " + chore)

# disconnect from the server
smtp_obj.quit()
