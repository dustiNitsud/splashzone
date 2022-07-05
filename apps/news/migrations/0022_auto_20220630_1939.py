# Generated by Django 3.1.6 on 2022-06-30 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0021_auto_20220630_1827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newspost',
            name='wwar',
        ),
        migrations.AddField(
            model_name='newspost',
            name='wwar_link',
            field=models.ManyToManyField(blank=True, to='news.WhatWeAreReading'),
        ),
        migrations.AddField(
            model_name='whatwearereading',
            name='news_post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='news.newspost'),
        ),
    ]
