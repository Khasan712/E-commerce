# Generated by Django 3.2 on 2021-12-30 21:06

from django.db import migrations
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='custom_user',
            name='location',
            field=location_field.models.plain.PlainLocationField(blank=True, max_length=63),
        ),
    ]