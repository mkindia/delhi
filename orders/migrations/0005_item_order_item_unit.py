# Generated by Django 4.1.1 on 2022-10-04 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_alter_item_item_unit'),
        ('orders', '0004_alter_item_order_packing_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='item_order',
            name='item_unit',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='items.unit'),
            preserve_default=False,
        ),
    ]
