# Generated by Django 3.2.8 on 2021-11-27 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0015_remove_lostinventorydata_li'),
    ]

    operations = [
        migrations.AddField(
            model_name='lostinventorydata',
            name='LIF',
            field=models.CharField(default='0', max_length=1000),
        ),
        migrations.AddField(
            model_name='lostinventorydata',
            name='LIM',
            field=models.CharField(default='0', max_length=1000),
        ),
        migrations.AddField(
            model_name='lostinventorydata',
            name='LISA',
            field=models.CharField(default='0', max_length=1000),
        ),
        migrations.AddField(
            model_name='lostinventorydata',
            name='LISU',
            field=models.CharField(default='0', max_length=1000),
        ),
        migrations.AddField(
            model_name='lostinventorydata',
            name='LIT',
            field=models.CharField(default='0', max_length=1000),
        ),
        migrations.AddField(
            model_name='lostinventorydata',
            name='LITH',
            field=models.CharField(default='0', max_length=1000),
        ),
        migrations.AddField(
            model_name='lostinventorydata',
            name='LIW',
            field=models.CharField(default='0', max_length=1000),
        ),
    ]
