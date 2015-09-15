# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('twilio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sms',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 3, 14, 28, 3, 711647, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=False,
        ),
    ]
