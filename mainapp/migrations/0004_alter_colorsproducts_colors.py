# Generated by Django 3.2 on 2022-01-04 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colorsproducts',
            name='colors',
            field=models.CharField(blank=True, max_length=220),
        ),
    ]