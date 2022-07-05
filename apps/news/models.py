import site
from tabnanny import verbose
from bs4 import BeautifulSoup
from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.utils import timezone
from django.conf import settings
from taxonomy.models import Topic
from lib.sitestuff import SiteModel
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class NewsPost(SiteModel):
    wwar = models.ForeignKey("WhatWeAreReading", default=1 ,on_delete=models.CASCADE)
    wwar_link = models.ManyToManyField('WhatWeAreReading', blank=True, related_name='wwar_link')
    title = models.CharField(max_length=300)
    body = models.TextField(max_length=6000)
    source = models.URLField()
    is_cover_story = models.BooleanField(default=False)
    publish_date = models.DateField(default=timezone.now)
    active = models.BooleanField(default=True)
    topics = models.ManyToManyField(Topic)
 
    def __str__(self):
        return '<{}> {}'.format(self.site.domain, self.title)
    
    @property
    def url(self):
        return reverse('newspost_detail', kwargs={'newspost_id': self.pk})

    @property
    def teaser(self):
        body_html = BeautifulSoup(self.body, 'html')
        body_html = body_html.text.replace('Dive Brief:', '')
        return body_html[:150]

    @property
    def has_topics(self):
        return self.topics.count() > 0

    @property
    def source_divesite(self):
        return self.site.name

    @classmethod
    def search(cls, topics=None, text_value=None):
        """Filters News Posts that match provided topics or text_value

            :param topics: QuerySet or List of Topic objects to filter against
            :type topics: QuerySet or List
            :param text_value: Search term to filter title or body against
            :type text_value: String

            :return: News Posts that match provided search terms
            :rtype: Queryset
        """
        results = cls.objects
        if topics:
            results = results.filter(topics__in=topics)
        if text_value:
            results = results.filter(Q(body__icontains=text_value) | Q(title__icontains=text_value))
        return set(results.all())


class WhatWeAreReading(models.Model):
    site_id = models.IntegerField(default=settings.SITE_ID)
    news_post = models.ForeignKey("NewsPost", default=1 ,on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    source = models.CharField(max_length=100)
    link = models.URLField()
    publish_date = models.DateField(default=timezone.now)

    class Meta:
        verbose_name = "What We Are Reading Link"

    def __str__(self):
        return self.title
    
    def clean(self):
        link_count = WhatWeAreReading.objects.filter(link=self.link).count()
        site_id_count = WhatWeAreReading.objects.filter(site_id=self.site_id).count()
        if site_id_count >=1 and self.pk != None:
            raise ValidationError("Link already exist for this dive site")


class WhatWeAreReadingLink(models.Model):
    news_post = models.ForeignKey('NewsPost', default=1 ,on_delete=models.CASCADE)
    wwar_link = models.ForeignKey('WhatWeAreReading', default = 1, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'News Post WWAR Links'
    
    def __str__(self):
        return str(self.wwar_link)
        