# Generated by Django 2.1.1 on 2018-09-28 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_event_capacity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='king',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='king', to='user.User_animal'),
        ),
    ]