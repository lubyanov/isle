# Generated by Django 2.0.7 on 2018-07-14 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isle', '0011_evententry_added_by_assistant'),
    ]

    operations = [
        migrations.AddField(
            model_name='evententry',
            name='check_in_pushed',
            field=models.BooleanField(default=False, verbose_name='Чекин проставлен в ILE'),
        ),
    ]
