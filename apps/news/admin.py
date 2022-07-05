import re
from django import forms
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from news.models import NewsPost, WhatWeAreReading, WhatWeAreReadingLink
from grappelli.forms import GrappelliSortableHiddenMixin
from django.conf import settings


class SourceInline(GrappelliSortableHiddenMixin, admin.TabularInline):
    model = WhatWeAreReadingLink
    exclude = ['site_id', 'publish_date']
    extra = 1
    max_num = 3
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)


class NewsPostForm(forms.ModelForm):
    model = NewsPost
    class Meta:
        fields = [
            'title',
            'body',
            'source',
            'is_cover_story',
            'publish_date',
            'topics',
            'active',
        ]
    
        


class WhatWeAreReadingForm(forms.ModelForm):
    class Meta:
        exclude = ['site_id']
        model = WhatWeAreReading
        fields = [
            'title',
            'source',
            'link',
            'publish_date',
        ]

class NewsPostAdmin(SummernoteModelAdmin):
    form = NewsPostForm
    inlines = [SourceInline]
    list_display = ['title', 'site', 'is_cover_story', 'active', 'has_topics']
    list_editable = ['is_cover_story', 'active']
    readonly_fields = ['site', ]
    summernote_fields = ['body', ]

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        
        for instance in instances:
            instance.save()
        formset.save_m2m()


class WhatWeAreReadingAdmin(admin.ModelAdmin):
    form = WhatWeAreReadingForm
    list_display = ['title', 'source', 'link']
    list_editable = ['source', 'link']
    


admin.site.register(NewsPost, NewsPostAdmin)
admin.site.register(WhatWeAreReading, WhatWeAreReadingAdmin)