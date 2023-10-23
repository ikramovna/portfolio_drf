# Generated by Django 4.2.6 on 2023-10-06 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('keyword', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('url', models.URLField()),
            ],
        ),
    ]
