# Generated by Django 4.0.4 on 2022-07-23 09:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_remove_item_order_order_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item_order',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
