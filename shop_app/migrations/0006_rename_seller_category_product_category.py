# Generated by Django 5.0 on 2024-01-29 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0005_rename_category_product_seller_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='seller_category',
            new_name='category',
        ),
    ]
