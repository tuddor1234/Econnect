# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-24 21:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('econnect', '0012_auto_20200524_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='img',
            field=models.ImageField(default='static/default_training.jpg', upload_to='trainingsPhoto'),
        ),
        migrations.AlterField(
            model_name='training',
            name='materials',
            field=models.FileField(upload_to='resources'),
        ),
        migrations.AlterField(
            model_name='training',
            name='next_session',
            field=models.DateTimeField(blank=True, max_length=128),
        ),
    ]
