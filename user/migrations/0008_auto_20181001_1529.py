# Generated by Django 2.1 on 2018-10-01 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
