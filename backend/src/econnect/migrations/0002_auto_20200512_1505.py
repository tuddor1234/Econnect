# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-12 12:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('econnect', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(default='default.jpg', upload_to='uploads')),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='No Name', max_length=120)),
                ('email', models.EmailField(default='No Email', max_length=254)),
                ('department', models.CharField(default='No Deptartment', max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training_name', models.CharField(max_length=128)),
                ('materials', models.FileField(upload_to='uploads')),
                ('next_session', models.DateTimeField(max_length=128)),
                ('trainer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='econnect.Trainer')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='No Name', max_length=120)),
                ('email', models.EmailField(default='No Email', max_length=254)),
                ('department', models.CharField(default='No Deptartment', max_length=120)),
            ],
        ),
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.AddField(
            model_name='profile',
            name='target_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='econnect.User'),
        ),
    ]
