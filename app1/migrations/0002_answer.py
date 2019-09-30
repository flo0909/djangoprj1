# Generated by Django 2.2.5 on 2019-09-30 16:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('content', models.TextField()),
                ('answered_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
