# Generated by Django 4.1.6 on 2023-03-07 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RX', '0004_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='invoice',
        ),
        migrations.AddField(
            model_name='order',
            name='Invoice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='invoice_order', to='RX.invoices'),
        ),
    ]
