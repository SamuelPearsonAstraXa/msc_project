from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.MoviesListView.as_view(), name='home'),
    path('create/', views.CreateMovieView.as_view(), name='create-movie'),
    path('create/actor/', views.CreateActorView.as_view(), name='create-actor'),
    path('create/genre/', views.CreateGenreView.as_view(), name='create-genre'),
    path('fetch-data/', views.fetch_data, name='fetch-data'),
    path('<str:id>/', views.MovieDetailView.as_view(), name='detail'),
]