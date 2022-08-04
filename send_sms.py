import os
from twilio.rest import Client

with open('credentials.txt') as file:
    sid = file.readline()
    token = file.readline()

print(sid, token)
# account_sid = os.environ['ACad9e4f80c786d3965ecb7b1ef54f9b97']
# account

# os.environ[]