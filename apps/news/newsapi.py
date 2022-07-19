from newsapi import NewsApiClient

from django.conf import settings


class NewsApiConnector:
    def __init__(self):
        self.instance = NewsApiClient(api_key=settings.NEWS_API_KEY)

    def sources(self):
        sources = self.instance.get_sources()
        return sources['sources']

    def headlines(self, country, page_size=100):
        return self.instance.get_top_headlines(country=country, page_size=page_size)['articles']
