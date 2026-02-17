from django.shortcuts import render
from django.http import JsonResponse
from .models import Series, Season, Episode
from django.views.generic import ListView, DetailView

class SeriesDetailView(DetailView):
    template_name = 'series/series_detail.html'
    model = Series
    pk_url_kwarg = 'id'
    context_object_name = 'series'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        context['related_series'] = Series.objects.all()
        return context

class SeriesListView(ListView):
    template_name = 'series/series_list.html'
    model = Series
    context_object_name = 'series_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Series'
        return context
    
def fetch_data(request):
    series = []
    m_results = Series.objects.all()
    for m_result in m_results:
        result = {
            'id': m_result.id,
            'title': m_result.title,
            'release_date': m_result.release_date,
            'poster': m_result.poster.url,
            'thumbnail': m_result.thumbnail.url,
            'description': m_result.description,
            'season_count': m_result.season_count,
            'slug': m_result.slug,
        }
        series.append(result)
    return JsonResponse({'my_response':'This is the response.','series':series})
