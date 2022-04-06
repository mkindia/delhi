# Generated by Django 4.0 on 2022-04-06 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consignee_order',
            name='order_date',
        ),
        migrations.AddField(
            model_name='consignee_order',
            name='create_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='consignee_order',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Date'),
        ),
    ]
