# Generated by Django 2.2.6 on 2019-11-05 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_article_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='image',
        ),
    ]
