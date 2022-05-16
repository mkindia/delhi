# Generated by Django 4.0 on 2022-05-13 16:12

import clients.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_remove_client_whatsapp_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consignee',
            name='consignee_name',
            field=clients.models.LowerCase(error_messages={'unique': 'A consignee already exists.'}, max_length=150),
        ),
    ]