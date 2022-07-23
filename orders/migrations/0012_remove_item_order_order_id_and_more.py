# Generated by Django 4.0.4 on 2022-07-22 14:50

from django.db import migrations
import orders.models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_alter_consignee_order_order_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item_order',
            name='order_id',
        ),
        migrations.RemoveField(
            model_name='item_order_status',
            name='order_id',
        ),
        migrations.RemoveField(
            model_name='item_order_transfer',
            name='order_id',
        ),
        migrations.AddField(
            model_name='item_order',
            name='order_type',
            field=orders.models.LowerCase(blank=True, choices=[('order', 'order'), ('purchase', 'purchase'), ('transferred', 'transferred')], default='order', max_length=30, null=True),
        ),
    ]
