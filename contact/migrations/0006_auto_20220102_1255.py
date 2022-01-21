# Generated by Django 3.2 on 2022-01-02 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_alter_ourbranch_short_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourbranch',
            name='comp_map',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='ourbranch',
            name='short_day',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
