# Generated by Django 2.2.5 on 2019-10-24 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0008_auto_20191024_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='off',
            field=models.DecimalField(decimal_places=2, default=0.1, max_digits=10),
        ),
    ]
