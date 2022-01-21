# Generated by Django 3.2 on 2021-12-30 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomments',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='blog.blogcomments'),
        ),
    ]