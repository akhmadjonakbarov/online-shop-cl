# Generated by Django 5.0 on 2024-01-30 16:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('location_app', '0001_initial'),
        ('shop_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='set_seller_orders', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='set_user_orders', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='orderitemlocation',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location_app.district'),
        ),
        migrations.AddField(
            model_name='orderitemlocation',
            name='order_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_app.orderitem'),
        ),
        migrations.AddField(
            model_name='orderitemlocation',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location_app.region'),
        ),
        migrations.AddField(
            model_name='product',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='set_products_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_app.product'),
        ),
        migrations.AddField(
            model_name='review',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='set_reviews_product', to='shop_app.product'),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='set_reviews_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sellercategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_app.category'),
        ),
        migrations.AddField(
            model_name='sellercategory',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='product',
            name='seller_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_app.sellercategory'),
        ),
    ]
