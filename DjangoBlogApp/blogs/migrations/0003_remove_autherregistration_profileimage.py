# Generated by Django 3.0.8 on 2020-07-24 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20200724_0911'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autherregistration',
            name='profileimage',
        ),
    ]