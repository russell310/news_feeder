from .models import country_from_newsapi, Sources
from .newsapi import NewsApiConnector
from .models import News

def update_news():
    items = []
    for item in country_from_newsapi:
        headlines = NewsApiConnector().headlines(country=item.lower(), page_size=100)
        for index, value in enumerate(headlines):
            source, created = Sources.objects.get_or_create(slug=value["source"]["id"],
                                                            defaults={'name': value["source"]["name"]})
            items.append(News(
                country=item,
                headline=value["title"],
                thumbnail=value["urlToImage"],
                source=source,
                url=value["url"]
            ))
    News.objects.bulk_update_or_create(items, ['headline', 'thumbnail'], match_field='url')

