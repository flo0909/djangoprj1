# Generated by Django 2.2.5 on 2019-10-24 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feature', '0002_ticket_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='discount',
            field=models.BooleanField(default=False),
        ),
    ]
