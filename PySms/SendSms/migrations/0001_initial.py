# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sms',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=160)),
                ('number', models.CharField(max_length=50)),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'date published')),
            ],
        ),
    ]
