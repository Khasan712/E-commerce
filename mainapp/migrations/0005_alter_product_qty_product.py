# Generated by Django 3.2 on 2022-01-10 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_alter_colorsproducts_colors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='qty_product',
            field=models.PositiveIntegerField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='1', max_length=2),
        ),
    ]
