from django.conf import settings

import twilio
import twilio.rest

def twilio_message (number,text):
	client = twilio.rest.TwilioRestClient(
		settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
	return client.messages.create(
		text=text,
		to=number,
		from_=settings.TWILIO_PHONE_NUMBER)