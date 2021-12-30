from twilio.rest import Client
from credentials1 import account_sid, auth_token, my_cell, my_twilio

tClient = Client(account_sid, auth_token)

## Multiple lines of the message
## my_msg = ''.join(['You have 10 messages\n' for i in range(10)])
my_msg = 'You have a new message'

message = tClient.messages.create(to=my_cell, from_=my_twilio, body=my_msg)
