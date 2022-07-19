from django.urls import path
from .views import NewsPreferenceView, NewsListView

urlpatterns = [
    path('', NewsListView.as_view(), name='home'),
    path('preference/', NewsPreferenceView.as_view(), name='news_preference')
]
