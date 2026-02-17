from django.urls import path
from . import views

app_name = 'series'

urlpatterns = [
    path('', views.SeriesListView.as_view(), name='home'),
    path('fetch-data/', views.fetch_data, name='fetch-data'),
    path('<str:id>/', views.SeriesDetailView.as_view(), name='detail'),
]