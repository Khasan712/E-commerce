# Generated by Django 3.2 on 2022-01-10 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0005_remove_custom_user_region'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='custom_user',
            name='location',
        ),
    ]
