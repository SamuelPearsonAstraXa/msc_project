from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.MoviesListView.as_view(), name='home'),
    path('fetch-data/', views.fetch_data, name='fetch-data'),
    path('<str:id>/', views.MovieDetailView.as_view(), name='detail'),
]