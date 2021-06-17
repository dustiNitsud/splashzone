# Generated by Django 3.1.6 on 2021-06-17 12:39

from django.db import migrations
from taxonomy.models import DiveSite, Topic
from wavepool.models import NewsPost


def forwards(apps, schema_editor):
    sites = DiveSite.objects.all()
    sites_dict = {s.url_name: s for s in sites}

    topics = Topic.objects.all()
    topics_dict = {t.internal_name: t for t in topics}

    posts = NewsPost.objects.all()
    for post in posts:
        for key, site in sites_dict.items():
            if key in post.source:
                post.divesite = site

        for key, topic in topics_dict.items():
            if key in post.source:
                post.topics.add(topic)

        post.save()


def backwards(apps, schema_editor):
    DiveSite.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('wavepool', '0004_newspost_divesite'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]
