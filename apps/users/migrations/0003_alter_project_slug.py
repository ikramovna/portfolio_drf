# Generated by Django 4.2.3 on 2023-07-18 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_project_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
