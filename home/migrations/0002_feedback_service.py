# Generated by Django 3.0.8 on 2020-07-26 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('image', models.CharField(blank=True, max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.TextField()),
                ('title', models.CharField(max_length=200)),
                ('upper_part', models.CharField(max_length=300)),
                ('lower_part', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
