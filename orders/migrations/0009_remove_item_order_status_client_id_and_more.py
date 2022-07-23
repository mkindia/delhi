# Generated by Django 4.0.4 on 2022-07-20 17:18

from django.db import migrations, models
import orders.models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_item_order_status_client_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item_order_status',
            name='client_id',
        ),
        migrations.RemoveField(
            model_name='item_order_status',
            name='consignee_id',
        ),
        migrations.AddField(
            model_name='consignee_order',
            name='Item_Order_Status_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='consignee_order',
            name='order_type',
            field=orders.models.LowerCase(blank=True, choices=[('sales', 'sales'), ('purchase', 'purchase'), ('transferred', 'transferred')], default='sales', max_length=30, null=True),
        ),
    ]