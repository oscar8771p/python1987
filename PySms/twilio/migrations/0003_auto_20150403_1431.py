# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('twilio', '0002_sms_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sms',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'date published'),
        ),
    ]
