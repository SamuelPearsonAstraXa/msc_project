from django.shortcuts import render
from .models import Series, Season, Episode
from django.views.generic import ListView

class SeriesListView(ListView):
    template_name = 'series/series_list.html'
    model = Series
    context_object_name = 'series_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Series'
        return context