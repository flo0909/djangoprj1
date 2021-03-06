# Generated by Django 2.2.5 on 2019-10-24 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_delete_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=250)),
                ('added', models.DateField(auto_now_add=True)),
                ('user_is_vip', models.BooleanField(default=True)),
            ],
        ),
    ]
