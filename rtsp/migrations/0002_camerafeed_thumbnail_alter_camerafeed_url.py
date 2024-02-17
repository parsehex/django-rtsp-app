# Generated by Django 5.0.2 on 2024-02-14 20:15

import rtsp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rtsp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='camerafeed',
            name='thumbnail',
            field=models.ImageField(default='default.jpg', upload_to='thumbnails/'),
        ),
        migrations.AlterField(
            model_name='camerafeed',
            name='url',
            field=rtsp.models.RTSPURLField(),
        ),
    ]