"""
ASGI config for news_feeder project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from apps.news.consumers import GetNewsConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_feeder.settings')

django_asgi_app = get_asgi_application()

wspatterns = [
    path('ws/news/', GetNewsConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    'websocket': AuthMiddlewareStack(
        URLRouter(
            wspatterns
        )
    )
})
