# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-26 19:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
        ('help_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='my_job',
            field=models.ManyToManyField(related_name='my_job', to='login_app.User'),
        ),
    ]
