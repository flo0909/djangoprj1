# Generated by Django 2.2.5 on 2019-10-16 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_usericon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usericon',
            name='icon',
            field=models.ImageField(upload_to='images/'),
        ),
    ]