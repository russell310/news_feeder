from django.core.management.base import BaseCommand

from apps.news.models import Sources
from apps.news.newsapi import NewsApiConnector


class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        sources = NewsApiConnector().sources()
        data = []
        for item in sources:
            data.append(Sources(
                name=item['name'],
                slug=item['id'],
                url=item['url'],
                country=item['country']
            ))

        Sources.objects.bulk_update_or_create(data, ['name', 'url', 'country'], match_field='slug')
