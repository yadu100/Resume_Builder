# Generated by Django 5.1.4 on 2025-01-15 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0013_remove_education_cgpa_remove_education_degree_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='cgpa1',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='degree1',
            field=models.CharField(max_length=700, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='end_date1',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='school1',
            field=models.CharField(max_length=700, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='start_date1',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='professionalexperience',
            name='company1',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='professionalexperience',
            name='end_date1',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='professionalexperience',
            name='job_description1',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='professionalexperience',
            name='location1',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='professionalexperience',
            name='start_date1',
            field=models.DateField(null=True),
        ),
    ]
