from twilio.rest import Client
import keys

client = Client(keys.account_sid, keys.auth_token)

TwilioNumber = "+15074163994"

mycellphone = "+12142260749"

# textmessage = client.messages.create(
#   to=mycellphone, from_=TwilioNumber, body="Hey There!")

# print(textmessage.status)

call = client.calls.create(
    url='https://demo/twilio.com/docs.voice.xml', to=mycellphone, from_=TwilioNumber)
