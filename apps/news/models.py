from bs4 import BeautifulSoup

from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.utils import timezone

from taxonomy.models import Topic
from lib.sitestuff import SiteModel


class NewsPost(SiteModel):
    title = models.CharField(max_length=300)
    body = models.TextField(max_length=3000)
    source = models.URLField()
    is_cover_story = models.BooleanField(default=False)
    publish_date = models.DateField(default=timezone.now)
    topics = models.ManyToManyField(Topic)
    active = models.BooleanField(default=True)

    def __str__(self):
        return '<{}> {}'.format(self.site.domain, self.title)

    @property
    def url(self):
        return reverse('newspost_detail', kwargs={'newspost_id': self.pk})

    @property
    def teaser(self):
        body_html = BeautifulSoup(self.body, 'html')
        return body_html.text[:150]

    @property
    def source_divesite(self):
        return self.divesite.display_name

    def tags(self):
        return [
            'HR', 'Diversity & Inclusion', 'Culture'
        ]

    @classmethod
    def search(cls, topics=None, text_value=None):
        results = cls.objects
        if topics:
            results = results.filter(topics__in=topics)
        if text_value:
            results = results.filter(Q(body__icontains=text_value) | Q(title__icontains=text_value))
        return set(results.all())
