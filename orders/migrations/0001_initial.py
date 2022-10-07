# Generated by Django 4.1.1 on 2022-10-07 14:43

from django.db import migrations, models
import django.db.models.deletion
import orders.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('items', '0001_initial'),
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item_Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_group', orders.models.LowerCase(default='d', max_length=10)),
                ('order_date', models.DateField()),
                ('item_veriant_price', models.DecimalField(decimal_places=2, default=1.1, max_digits=7)),
                ('item_qty', models.DecimalField(decimal_places=1, default=0, max_digits=7)),
                ('order_type', orders.models.LowerCase(blank=True, default='or', max_length=30, null=True)),
                ('item_order_status_id', models.PositiveBigIntegerField(blank=True, null=True)),
                ('create_date', models.DateField(auto_now_add=True, null=True)),
                ('comment', orders.models.LowerCase(blank=True, max_length=200, null=True)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.client')),
                ('consignee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.consignee')),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='items.item')),
                ('item_unit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='items.unit')),
                ('item_variant_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='items.item_variant')),
                ('packing_unit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='items.packing_unit')),
            ],
        ),
        migrations.CreateModel(
            name='Item_Order_Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('item_qty', models.DecimalField(decimal_places=1, default=0, max_digits=7)),
                ('create_date', models.DateField(auto_now_add=True, null=True)),
                ('status', orders.models.LowerCase(blank=True, default='dis', max_length=30, null=True)),
                ('item_order_trn_id', models.PositiveBigIntegerField(blank=True, null=True)),
                ('docket_number', orders.models.LowerCase(blank=True, max_length=50, null=True)),
                ('state', orders.models.LowerCase(blank=True, max_length=64, null=True, verbose_name='state')),
                ('station', orders.models.LowerCase(blank=True, max_length=64, null=True, verbose_name='station')),
                ('transport', orders.models.LowerCase(blank=True, max_length=64, null=True, verbose_name='transport')),
                ('private_marka', models.CharField(blank=True, max_length=100, null=True)),
                ('comment', orders.models.LowerCase(blank=True, max_length=200, null=True)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.client')),
                ('consignee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consignee_id', to='clients.consignee')),
                ('item_order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.item_order')),
                ('transfer_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tranfer_id', to='clients.consignee')),
            ],
        ),
        migrations.CreateModel(
            name='Consignee_Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_type', orders.models.LowerCase(blank=True, default='or', max_length=30, null=True)),
                ('create_date', models.DateField(auto_now_add=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('Item_Order_Status_id', models.PositiveIntegerField(blank=True, null=True)),
                ('comment', orders.models.LowerCase(blank=True, max_length=200, null=True)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.client')),
                ('consignee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.consignee')),
            ],
        ),
    ]
