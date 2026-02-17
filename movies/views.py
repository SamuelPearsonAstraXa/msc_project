from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from .models import Movie

class MovieDetailView(DetailView):
    template_name = 'movies/movie_detail.html'
    model = Movie
    pk_url_kwarg = 'id'
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        context['related_movies'] = Movie.objects.all()
        return context

class MoviesListView(ListView):
    template_name = 'movies/movies_list.html'
    model = Movie
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Movies'
        return context
    
def fetch_data(request):
    movies = []
    m_results = Movie.objects.all()
    for m_result in m_results:
        result = {
            'id': m_result.id,
            'title': m_result.title,
            'release_date': m_result.release_date,
            'poster': m_result.poster.url,
            'thumbnail': m_result.thumbnail.url,
            'description': m_result.description,
            'duration': m_result.duration,
            'rating': m_result.rating,
            # 'genres': m_result.genres,
            # 'cast': m_result.cast,
            'create_date': m_result.create_date,
            'slug': m_result.slug,
        }
        movies.append(result)
    return JsonResponse({'my_response':'This is the response.','movies':movies})
