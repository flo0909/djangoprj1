# Generated by Django 2.2.5 on 2019-10-16 02:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_userpost_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpost',
            name='image',
        ),
    ]
