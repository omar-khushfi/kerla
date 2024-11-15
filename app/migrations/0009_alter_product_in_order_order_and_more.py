# Generated by Django 5.1.2 on 2024-10-25 16:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_product_in_order_order_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_in_order',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.order'),
        ),
        migrations.AlterField(
            model_name='product_in_order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product'),
        ),
    ]