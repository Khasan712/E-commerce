# Generated by Django 3.2 on 2022-01-11 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address_line_2',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_note',
            field=models.TextField(blank=True, max_length=250),
        ),
    ]