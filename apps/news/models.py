from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django_countries import countries
from django_countries.fields import CountryField
from multiselectfield import MultiSelectField
from bulk_update_or_create import BulkUpdateOrCreateQuerySet
from apps.news.newsapi import NewsApiConnector

User = get_user_model()

country_from_newsapi = ['AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BR', 'CA', 'CH', 'CN', 'CO', 'CU', 'CZ', 'DE', 'EG', 'FR',
                        'GB', 'GR', 'HK', 'HU', 'ID', 'IE', 'IL', 'IN', 'IT', 'JP', 'KR', 'LT', 'LV', 'MA', 'MX', 'MY',
                        'NG', 'NL', 'NO', 'NZ', 'PH', 'PL', 'PT', 'RO', 'RS', 'RU', 'SA', 'SE', 'SG', 'SI', 'SK', 'TH',
                        'TR', 'TW', 'UA', 'US', 'VE', 'ZA']

dictfilter = lambda x, y: dict([(i, x[i]) for i in x if i in set(y)])
filtered_country = dictfilter(dict(countries), country_from_newsapi)
COUNTRY_CHOICES = [(k, v) for k, v in filtered_country.items()]


class Sources(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    country = CountryField(null=True, blank=True)
    objects = BulkUpdateOrCreateQuerySet.as_manager()

    def __str__(self):
        return self.name


class NewsPreference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    country = MultiSelectField(choices=COUNTRY_CHOICES)
    source = models.ManyToManyField(Sources, blank=True)


class News(models.Model):
    headline = models.CharField(max_length=255)
    country = CountryField()
    thumbnail = models.CharField(max_length=1000, null=True, blank=True)
    source = models.ForeignKey(Sources, on_delete=models.CASCADE, null=True, blank=True)
    url = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = BulkUpdateOrCreateQuerySet.as_manager()

    def __str__(self):
        return self.headline
