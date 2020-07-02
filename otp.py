import twilio
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import random # generate random number
otp = random.randint(1000,9999)
print("Your OTP is - ",otp)
# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'account_sid'
auth_token = 'token_id'
client = Client(account_sid, auth_token)

message = client.messages.create(
         body='Hello Mr. Mayur Your Secure Device OTP is - ' + str(otp) + 'now your mobile is hacked!\n Byby...',
         from_='your twilio number along with country code',
         to='Number on which you want to send otp with country code'
     )

print(message.sid)
