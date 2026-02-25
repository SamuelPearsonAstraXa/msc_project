from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Series, Season, Episode
from .forms import CreateSeriesForm, CreateSeasonForm, CreateEpisodeForm, UpdateSeriesForm

class DeleteSeriesView(PermissionRequiredMixin, DeleteView):
    permission_required = 'request.user.is_staff'
    template_name = 'series/delete_series.html'
    model = Series
    context_object_name = 'series'
    pk_url_kwarg = 'id'
    success_url = '/series/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Delete {self.object.title}'
        return context

class CreateEpisodeView(PermissionRequiredMixin, CreateView):
    permission_required = 'request.user.is_staff'
    form_class = CreateEpisodeForm
    template_name = 'series/create_episode.html'
    success_url = '/accounts/admin-dashboard/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create an episode'
        return context

class CreateSeasonView(PermissionRequiredMixin, CreateView):
    permission_required = 'request.user.is_staff'
    form_class = CreateSeasonForm
    template_name = 'series/create_season.html'
    success_url = '/accounts/admin-dashboard/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create a season'
        return context

class UpdateSeriesView(PermissionRequiredMixin, UpdateView):
    permission_required = 'request.user.is_staff'
    model = Series
    form_class = UpdateSeriesForm
    template_name = 'series/update_series.html'
    success_url = '/series/'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update a series'
        return context

class CreateSeriesView(PermissionRequiredMixin, CreateView):
    permission_required = 'request.user.is_staff'
    form_class = CreateSeriesForm
    template_name = 'series/create_series.html'
    success_url = '/accounts/admin-dashboard/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create a series'
        return context

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
