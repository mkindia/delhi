# Generated by Django 4.0 on 2022-05-10 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_client_whatsapp_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='whatsapp_number',
        ),
        migrations.AlterField(
            model_name='consignee',
            name='station',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.station'),
        ),
        migrations.AlterField(
            model_name='consignee',
            name='transport',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.transport'),
        ),
    ]