from django.urls import path
from . import views

app_name = 'series'

urlpatterns = [
    path('', views.SeriesListView.as_view(), name='home'),
    path('create/', views.CreateSeriesView.as_view(), name='create-series'),
    path('create/season/', views.CreateSeasonView.as_view(), name='create-season'),
    path('create/episode/', views.CreateEpisodeView.as_view(), name='create-episode'),
    path('fetch-data/', views.fetch_data, name='fetch-data'),
    path('<str:id>/', views.SeriesDetailView.as_view(), name='detail'),
    path('<str:id>/delete/', views.DeleteSeriesView.as_view(), name='delete-series'),
    path('<str:id>/update/', views.UpdateSeriesView.as_view(), name='update-series'),
]