# Generated by Django 5.1.4 on 2025-01-14 10:59

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0006_alter_professionalexperience_start_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('user', models.CharField(max_length=150)),
                ('degree', models.CharField(max_length=700)),
                ('school', models.CharField(max_length=700)),
                ('cgpa', models.FloatField()),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hobbies',
            fields=[
                ('user', models.CharField(max_length=150)),
                ('hobbies', models.TextField(max_length=1000)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('user', models.CharField(max_length=150)),
                ('languages', models.TextField(max_length=1000)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('user', models.CharField(max_length=150)),
                ('skills', models.TextField(max_length=1000)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
