# Generated by Django 3.0.8 on 2020-08-10 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200808_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='telephone',
            field=models.IntegerField(),
        ),
    ]
