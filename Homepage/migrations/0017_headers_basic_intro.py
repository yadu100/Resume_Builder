# Generated by Django 5.1.4 on 2025-01-16 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0016_remove_headers_basic_intro'),
    ]

    operations = [
        migrations.AddField(
            model_name='headers',
            name='basic_intro',
            field=models.TextField(blank=True, max_length=3000, null=True),
        ),
    ]
