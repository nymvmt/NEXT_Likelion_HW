# Generated by Django 4.1 on 2022-08-08 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_author_post_create_dt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='create_dt',
        ),
    ]
