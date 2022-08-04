from email import message
from twilio.rest import Client

with open('credentials.txt') as file:
    account_sid = file.readline()
    auth_token = file.readline()
    my_twilio_num = file.readline()
    recipient_num = file.readline()

client = Client(account_sid,auth_token)

message = client.messages \
                .create(
                    body="This is a test message from Seth using Twilio in a Python script",
                    from_=my_twilio_num,
                    to=recipient_num
                )

print(message.sid)