# Generated by Django 4.0.4 on 2022-07-04 14:50

from django.db import migrations
import django.utils.timezone
import items.models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='short_unit_name',
            field=items.models.LowerCase(default=django.utils.timezone.now, max_length=10, unique=True),
            preserve_default=False,
        ),
    ]
