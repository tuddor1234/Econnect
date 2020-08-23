# Generated by Django 3.0.6 on 2020-08-18 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('econnect', '0019_auto_20200814_1416'),
    ]

    operations = [
        migrations.CreateModel(
            name='Completion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datecompleted', models.DateTimeField()),
                ('trainingcompleted', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='econnect.Training')),
            ],
        ),
    ]