# Generated by Django 3.0.8 on 2020-08-17 03:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_checkout_checkout'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='Total_price',
            new_name='price',
        ),
    ]
