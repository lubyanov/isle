# Generated by Django 2.0.7 on 2018-09-21 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('isle', '0032_auto_20180827_2247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='ile_id',
        ),
        migrations.RemoveField(
            model_name='event',
            name='ile_id',
        ),
    ]