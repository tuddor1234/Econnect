# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-24 16:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('econnect', '0009_auto_20200524_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='materials',
            field=models.FileField(blank=True, upload_to='{{training_name}}/resources'),
        ),
    ]
