# Generated by Django 3.2.8 on 2021-11-18 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_hero_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hero',
            name='alias',
        ),
        migrations.RemoveField(
            model_name='hero',
            name='location',
        ),
    ]
