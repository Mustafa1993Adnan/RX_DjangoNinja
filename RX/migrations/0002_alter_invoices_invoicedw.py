# Generated by Django 4.1.6 on 2023-03-04 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RX', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoices',
            name='InvoiceDW',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='RX.distributorwarehouse'),
        ),
    ]