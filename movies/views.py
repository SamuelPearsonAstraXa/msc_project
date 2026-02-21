from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Movie, Actor, Genre
from .forms import CreateMovieForm, CreateActorForm, CreateGenreForm

class DeleteMovieView(DeleteView):
    template_name = 'movies/delete_movie.html'
    model = Movie
    context_object_name = 'movie'
    pk_url_kwarg = 'id'
    success_url = '/movies/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Delete {self.object.title}'
        return context

class CreateGenreView(CreateView):
    form_class = CreateGenreForm
    template_name = 'movies/create_genre.html'
    success_url = '/accounts/admin-dashboard/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create genre'
        return context
    
class CreateActorView(CreateView):
    form_class = CreateActorForm
    template_name = 'movies/create_actor.html'
    success_url = '/accounts/admin-dashboard/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create actor'
        return context

class CreateMovieView(CreateView):
    form_class = CreateMovieForm
    template_name = 'movies/create_movie.html'
    success_url = '/accounts/admin-dashboard/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create movie'
        return context

class ActorDetailView(DetailView):
    template_name = 'movies/actor_detail.html'
    model = Actor
    pk_url_kwarg = 'id'
    context_object_name = 'actor'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.name
        context['featured_movies'] = Movie.objects.all().order_by('-create_date')
        return context

class ActorsListView(ListView):
    template_name = 'movies/actors_list.html'
    model = Movie
    context_object_name = 'actors'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actors'
        return context

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
    
def fetch_actors(request):
    actors = []
    a_results = Actor.objects.all()
    for a_result in a_results:
        result = {
            'id': a_result.id,
            'name': a_result.name,
            'bio': a_result.bio,
            'photo': a_result.photo.url,
            'thumbnail': a_result.thumbnail.url,
            'slug': a_result.slug,
        }
        actors.append(result)
    return JsonResponse({'my_response':'This is the response.','actors':actors})
    
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
