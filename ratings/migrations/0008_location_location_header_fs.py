# Generated by Django 4.2.1 on 2023-05-22 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0007_location_header_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='location_header_fs',
            field=models.IntegerField(default=30),
        ),
    ]
