import itertools

import django_tables2 as tables
from django.utils.html import format_html
from .models import News


class NewsTable(tables.Table):
    counter = tables.Column(empty_values=(), verbose_name='#', attrs={
        'td': {
            'width': 20,
            'class': 'text-center'
        }
    })
    thumbnail = tables.Column(empty_values=(), verbose_name='Image', attrs={
        'td': {
            'width': 80,
            'class': 'text-center'
        }
    })
    headline = tables.Column(empty_values=(), verbose_name='Headline')

    def render_counter(self):
        self.row_counter = getattr(self, 'row_counter', itertools.count(self.page.start_index()))
        return next(self.row_counter)

    def render_thumbnail(self, record):
        if record.thumbnail:
            return format_html(
                '<img src="{url}" class="img-thumbnail">',
                url=record.thumbnail
            )
        else:
            return ''

    def render_headline(self, record):
        return format_html(
            '<a href="{url}">{headline}</a>',
            url=record.url,
            headline=record.headline
        )

    class Meta:
        model = News
        template_name = "django_tables2/bootstrap.html"
        fields = ('counter', 'thumbnail', 'headline', 'country', 'source')
        empty_text = 'There are no data yet'
        orderable = False
