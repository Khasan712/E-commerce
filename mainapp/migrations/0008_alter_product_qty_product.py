# Generated by Django 3.2 on 2022-01-10 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_alter_product_qty_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='qty_product',
            field=models.PositiveIntegerField(blank=True, default='1', null=True),
        ),
    ]