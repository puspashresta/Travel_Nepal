# Generated by Django 3.0.8 on 2020-08-11 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_book_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='price',
            new_name='Total_price',
        ),
    ]
