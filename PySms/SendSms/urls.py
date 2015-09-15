from django.conf.urls import url
from SendSms import views

urlpatterns = [
	url(r'^$',views.index, name='index'),
	url(r'^sms$',views.sms_list, name='sms'),
]