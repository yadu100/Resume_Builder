# Generated by Django 5.1.4 on 2025-01-14 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0002_headers_created_headers_user_alter_headers_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headers',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='headers',
            name='user',
            field=models.CharField(max_length=150),
        ),
    ]
