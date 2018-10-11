# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-09-22 19:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_contact', models.CharField(max_length=100)),
                ('email_contact', models.EmailField(max_length=254)),
                ('text_contact', models.TextField()),
                ('create_date_contact', models.DateTimeField(default=datetime.datetime(2018, 9, 22, 19, 0, 2, 932341, tzinfo=utc))),
            ],
        ),
    ]
