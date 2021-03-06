# Generated by Django 4.0.4 on 2022-07-21 17:29

from django.db import migrations
import orders.models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_item_order_status_client_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consignee_order',
            name='order_type',
            field=orders.models.LowerCase(blank=True, choices=[('order', 'order'), ('purchase', 'purchase'), ('transferred', 'transferred')], default='order', max_length=30, null=True),
        ),
    ]
