import operator
from functools import reduce

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.detail import SingleObjectTemplateResponseMixin
from django.views.generic.edit import ModelFormMixin, ProcessFormView
from django_tables2 import SingleTableView

from .forms import NewsPreferenceForm
from .models import NewsPreference, News

# Create your views here.
from .tables import NewsTable


class NewsPreferenceView(LoginRequiredMixin, SingleObjectTemplateResponseMixin, ModelFormMixin, ProcessFormView):
    form_class = NewsPreferenceForm
    model = NewsPreference
    template_name = 'add.html'
    page_title = 'News Preference'
    success_url = reverse_lazy('news_preference')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Preference'
        return context

    def get_object(self, queryset=None):
        try:
            return NewsPreference.objects.filter(user=self.request.user).first()
        except AttributeError:
            return None

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class NewsListView(LoginRequiredMixin, SingleTableView):
    model = News
    table_class = NewsTable
    template_name = 'list.html'

    def get_queryset(self):
        if NewsPreference.objects.filter(user=self.request.user).exists():
            np = NewsPreference.objects.filter(user=self.request.user).first()
            return News.objects.filter(country__in=list(np.country), source__in=list(np.source.values_list(flat=True)))
        return News.objects.none()

    def get(self, request, *args, **kwargs):
        data = super(NewsListView, self).get(request, *args, **kwargs)
        if not NewsPreference.objects.filter(user=self.request.user).exists():
            return redirect('news_preference')
        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'News Headlines'
        return context
