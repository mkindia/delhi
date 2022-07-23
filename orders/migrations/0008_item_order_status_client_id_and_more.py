# Generated by Django 4.0.4 on 2022-07-13 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_alter_consignee_client_id'),
        ('orders', '0007_alter_item_order_item_veriant_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item_order_status',
            name='client_id',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='clients.client'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item_order_status',
            name='consignee_id',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='clients.consignee'),
            preserve_default=False,
        ),
    ]
