from django.urls import path
from . import views

app_name = 'series'

urlpatterns = [
    path('', views.SeriesListView.as_view(), name='home'),
]