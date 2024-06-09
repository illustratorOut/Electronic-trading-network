# Generated by Django 5.0.6 on 2024-06-09 21:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0003_alter_supplier_options_alter_supplier_levels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='supply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='suppliers.supplier', verbose_name='Поставщик'),
        ),
    ]