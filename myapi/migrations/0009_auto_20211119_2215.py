# Generated by Django 3.2.8 on 2021-11-19 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0008_crimedetectiondata_lostinventorydata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crimedetectiondata',
            old_name='CD',
            new_name='LI',
        ),
        migrations.RemoveField(
            model_name='crimedetectiondata',
            name='DOW',
        ),
        migrations.RemoveField(
            model_name='lostinventorydata',
            name='DOW',
        ),
    ]
