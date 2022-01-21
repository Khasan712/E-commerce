# Generated by Django 3.2 on 2021-12-28 19:31

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('date_modified', models.DateTimeField(auto_now=True, null=True)),
                ('date_published', models.DateTimeField(auto_now_add=True, null=True)),
                ('title', models.CharField(max_length=500)),
                ('text', models.TextField()),
                ('blog_author', models.ForeignKey(default='admin', on_delete=django.db.models.deletion.CASCADE, related_name='blog_author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=200)),
                ('date_modified', models.DateTimeField(auto_now=True, null=True)),
                ('date_published', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='png', keep_meta=True, quality=75, size=[1000, 1000], upload_to='media/blog/imahes')),
                ('date_modified', models.DateTimeField(auto_now=True, null=True)),
                ('date_published', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogVideos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(blank=True, upload_to='media/blog/videos', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])])),
                ('date_modified', models.DateTimeField(auto_now=True, null=True)),
                ('date_published', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('message', models.TextField()),
                ('date_modified', models.DateTimeField(auto_now=True, null=True)),
                ('date_published', models.DateTimeField(auto_now_add=True, null=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.blog')),
                ('comment_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_author', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='blog.blogcomments')),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_category',
            field=models.ManyToManyField(related_name='blog_category', to='blog.BlogCategory'),
        ),
        migrations.AddField(
            model_name='blog',
            name='images',
            field=models.ManyToManyField(blank=True, to='blog.BlogImages'),
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='blog',
            name='video',
            field=models.ManyToManyField(blank=True, to='blog.BlogVideos'),
        ),
    ]
