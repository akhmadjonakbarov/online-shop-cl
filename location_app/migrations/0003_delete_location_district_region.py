# Generated by Django 5.0 on 2023-12-23 16:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location_app', '0002_district_region'),
        ('user_app', '0005_remove_userlocation_location_userlocation_district_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.AddField(
            model_name='district',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location_app.region'),
        ),
    ]
