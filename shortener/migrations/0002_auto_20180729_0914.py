# Generated by Django 2.0.7 on 2018-07-29 09:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urldetails',
            name='update',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
