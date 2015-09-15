from django.db import models
from datetime import datetime

# Create your models here.
class Sms(models.Model):
	text = models.CharField(max_length=160)
	number = models.CharField(max_length=50)
	pub_date = models.DateTimeField('date published', default=datetime.now)

	def __unicode__(self):
		return "%s ===> %s" % (self.number, self.text)
