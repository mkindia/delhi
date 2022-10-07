# Generated by Django 4.1.1 on 2022-10-07 14:43

from django.db import migrations, models
import django.db.models.deletion
import items.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_code', items.models.LowerCase(blank=True, max_length=100, null=True)),
                ('item_name', items.models.LowerCase(max_length=100, unique=True)),
                ('item_img', models.ImageField(blank=True, null=True, upload_to='item')),
                ('hsn_sac', items.models.LowerCase(blank=True, max_length=50, null=True)),
                ('is_active', models.BooleanField(blank=True, default=True, null=True)),
                ('item_discraption', items.models.LowerCase(blank=True, max_length=200, null=True)),
                ('comment', items.models.LowerCase(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item_Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', items.models.LowerCase(max_length=100, unique=True)),
                ('group_des', items.models.LowerCase(max_length=200)),
                ('comment', items.models.LowerCase(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Packing_Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('packing_unit_name', items.models.LowerCase(max_length=30)),
                ('packing_unit_abbreviation', items.models.LowerCase(default='cr', max_length=10)),
                ('packing_unit_des', items.models.LowerCase(max_length=200)),
                ('packing_unit_comment', items.models.LowerCase(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_name', items.models.LowerCase(max_length=30)),
                ('unit_abbreviation', items.models.LowerCase(max_length=10)),
                ('unit_des', items.models.LowerCase(max_length=100)),
                ('unit_comment', items.models.LowerCase(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Item_Variant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variant_code', items.models.LowerCase(blank=True, max_length=100, null=True)),
                ('variant_name', items.models.LowerCase(max_length=100)),
                ('item_variant_img', models.ImageField(blank=True, null=True, upload_to='itemvariant')),
                ('weight_kg', models.DecimalField(blank=True, decimal_places=3, default=1, max_digits=7, null=True)),
                ('height_cm', models.DecimalField(blank=True, decimal_places=2, default=1, max_digits=7, null=True)),
                ('length_cm', models.DecimalField(blank=True, decimal_places=2, default=1, max_digits=7, null=True)),
                ('width_cm', models.DecimalField(blank=True, decimal_places=2, default=1, max_digits=7, null=True)),
                ('depth_cm', models.DecimalField(blank=True, decimal_places=2, default=1, max_digits=7, null=True)),
                ('variant_color', items.models.LowerCase(blank=True, max_length=50, null=True)),
                ('master_packing', models.DecimalField(blank=True, decimal_places=0, default=1, max_digits=4, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=1, max_digits=7, null=True)),
                ('client_price_a', models.DecimalField(blank=True, decimal_places=2, default=1, max_digits=7, null=True)),
                ('client_price_b', models.DecimalField(blank=True, decimal_places=2, default=1, max_digits=7, null=True)),
                ('client_price_c', models.DecimalField(blank=True, decimal_places=2, default=1, max_digits=7, null=True)),
                ('client_price_d', models.DecimalField(blank=True, decimal_places=2, default=1, max_digits=7, null=True)),
                ('variant_stock', models.DecimalField(blank=True, decimal_places=2, default=1, max_digits=7, null=True)),
                ('is_active', models.BooleanField(blank=True, default=True, null=True)),
                ('variant_discraption', items.models.LowerCase(blank=True, max_length=200, null=True)),
                ('comment', items.models.LowerCase(blank=True, max_length=200, null=True)),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='items.item')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='item_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='items.item_group'),
        ),
        migrations.AddField(
            model_name='item',
            name='item_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='items.unit'),
        ),
    ]
