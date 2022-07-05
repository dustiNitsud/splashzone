# Generated by Django 3.1.6 on 2022-06-21 22:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_newspost_topics'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhatWeAreReading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('source', models.CharField(max_length=100)),
                ('link', models.URLField()),
                ('publish_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
