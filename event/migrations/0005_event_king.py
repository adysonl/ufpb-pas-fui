# Generated by Django 2.1.1 on 2018-09-28 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_remove_event_king'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='king',
            field=models.IntegerField(null=True),
        ),
    ]