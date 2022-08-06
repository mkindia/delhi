# Generated by Django 4.0.4 on 2022-08-04 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_alter_consignee_client_id'),
        ('orders', '0014_rename_order_unit_item_order_order_unit_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item_order_status',
            name='transfer_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tranfer_id', to='clients.consignee'),
        ),
    ]
