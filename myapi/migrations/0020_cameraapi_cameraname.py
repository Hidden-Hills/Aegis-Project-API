# Generated by Django 3.2.8 on 2021-12-01 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0019_auto_20211127_0547'),
    ]

    operations = [
        migrations.AddField(
            model_name='cameraapi',
            name='cameraName',
            field=models.CharField(default='Camera', max_length=100),
        ),
    ]
