from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from .models import country_from_newsapi, Sources
from .newsapi import NewsApiConnector
from .models import News
from celery import shared_task

channel_layer = get_channel_layer()


@shared_task(name='update_news')
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

    async_to_sync(channel_layer.group_send)(
        'news', {
            'type': 'send_news',
            'text': 'done'
        }
    )