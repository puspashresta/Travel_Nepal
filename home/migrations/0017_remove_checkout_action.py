# Generated by Django 3.0.8 on 2020-08-13 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20200813_1348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='action',
        ),
    ]