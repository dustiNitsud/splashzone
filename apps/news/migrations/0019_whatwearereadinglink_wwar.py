# Generated by Django 3.1.6 on 2022-06-28 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0018_whatwearereadinglink_news_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='whatwearereadinglink',
            name='wwar',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='news.whatwearereading'),
        ),
    ]
