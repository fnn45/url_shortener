# Generated by Django 2.0.7 on 2018-07-29 09:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0004_auto_20180729_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urldetails',
            name='timestamp',
            field=models.DateField(default=datetime.datetime(2018, 7, 29, 9, 34, 37, 534990, tzinfo=utc)),
        ),
    ]