# Generated by Django 2.2.6 on 2019-11-01 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('title_en', models.CharField(max_length=100)),
                ('audience', models.CharField(max_length=15)),
                ('open_date', models.DateTimeField()),
                ('genre', models.CharField(max_length=20)),
                ('watch_grade', models.CharField(max_length=20)),
                ('score', models.CharField(max_length=5)),
                ('poster_url', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
    ]