# Generated by Django 4.0 on 2022-04-13 14:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_rename_client_client_client_name_client_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='whatsapp_number',
            field=models.CharField(blank=True, max_length=16, null=True, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]