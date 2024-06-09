# Generated by Django 5.0.6 on 2024-06-09 10:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_initial'),
        ('suppliers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор поставщика'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='product',
            field=models.ManyToManyField(to='products.product', verbose_name='Продукт'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='supply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='suppliers.supplier', verbose_name='Поставщик'),
        ),
    ]