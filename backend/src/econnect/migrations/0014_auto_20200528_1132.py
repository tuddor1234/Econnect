# Generated by Django 3.0.4 on 2020-05-28 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('econnect', '0013_auto_20200525_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='static/default.png', upload_to='profile_pics'),
        ),
    ]