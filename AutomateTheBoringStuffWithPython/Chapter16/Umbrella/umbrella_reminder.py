"""Umbrella Reminder

Requests data from the api of http://www.openweathermap.org. Runs at 6 o'clock every day and checks
whether it's raining. If so texts you a reminder to pack an umbrella before leaving the house.

User needs to sign up for the api service and acquire his/her api key for authentication.

Twilio is used to send text messages, user needs to sign up for authentication.

--> cronjob to run every morning
0 6 * * * /<pathTo>/python3 /<pathTo>/umbrella_reminder.py > /<pathTo>/Umbrella/crontab.log 2>&1
"""

import json
import requests

from twilio.rest import Client

# change the city to where you live
city = 'istanbul'

# send a requests, returns json
response = requests.get(
    'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&APPID=<apikey>')

# turn requests text response to json data
weather = json.loads(response.text)

# settings for twilio account
account_SID = "<account_SID from twilio>"
auth_token = "<auth_token from twilio>"
message_body = "Don't forget to take your umbrella! Possible rain :)"

# send message if rain is possible
for w in ("rain", "thunder", "storm", "haze"):
    if w in weather["weather"][0]["main"].lower() or w in weather["weather"][0]["description"].lower():
        client = Client(account_SID, auth_token)
        client.messages.create(
            to="+905387648540",
            from_="+13862043689",
            body=message_body
        )
