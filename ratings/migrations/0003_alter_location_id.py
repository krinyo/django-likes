# Generated by Django 4.2.1 on 2023-05-22 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0002_remove_location_location_background_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]