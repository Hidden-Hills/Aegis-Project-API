# Generated by Django 3.2.8 on 2021-11-26 04:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0011_cameraapi'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crimedetectiondata',
            old_name='LI',
            new_name='CS',
        ),
    ]
