# Generated by Django 5.0 on 2023-12-18 16:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location_app', '0001_initial'),
        ('user_app', '0002_customuser_user_app_cu_email_7f86d4_idx'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveIndex(
            model_name='customuser',
            name='user_app_cu_email_7f86d4_idx',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='email',
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_seller',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='phonenumber',
            field=models.CharField(default=0, max_length=9, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userlocation',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location_app.location'),
        ),
        migrations.AddField(
            model_name='userlocation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
