# Generated by Django 5.1.4 on 2025-01-17 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0017_headers_basic_intro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='user',
            field=models.CharField(max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='headers',
            name='user',
            field=models.CharField(max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='hobbies',
            name='user',
            field=models.CharField(max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='languages',
            name='user',
            field=models.CharField(max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='professionalexperience',
            name='user',
            field=models.CharField(max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='skills',
            name='user',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
