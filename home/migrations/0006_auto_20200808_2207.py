# Generated by Django 3.0.8 on 2020-08-08 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_message_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='image',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]
