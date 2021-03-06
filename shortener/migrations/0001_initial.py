# Generated by Django 2.0.7 on 2018-07-28 20:24

from django.db import migrations, models
import shortener.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrlDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=220, validators=[shortener.validators.validate_url])),
                ('shortcode', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('description_text', models.TextField(blank=True, null=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
