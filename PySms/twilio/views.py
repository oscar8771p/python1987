import os

from django.shortcuts import render
# Create your views here.
from .models import Sms

print os.environ.get('TWILIO_ACCOUNT_SID')

print os.environ.get('TWILIO_AUTH_TOKEN')

def index(request):
	context = {'message': "Ready to send a message"}
	if request.method == 'POST':
		message = request.POST['message']
		number = request.POST['number']
		if message and number:
			context["message"] = "One message has been sent. Ready for another one...."
	return render(request,'twilio/index.html',context)

def sms_list(request):
	latest_sms = Sms.objects.order_by('-pub_date')[:5]
	context = {'latest_sms': latest_sms}
	return render(request,'twilio/sms.html',context)
