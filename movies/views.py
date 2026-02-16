from django.shortcuts import render
from django.views.generic import ListView
from .models import Movie

class MoviesListView(ListView):
    template_name = 'movies/movies_list.html'
    model = Movie
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Movies'
        return context