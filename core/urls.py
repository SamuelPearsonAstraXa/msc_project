from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('fetch_posts/', views.fetch_posts, name='fetch-data'),
    path('contact/', views.ContactUsView.as_view(), name='contact'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('fetch_search_results/', views.fetch_search_results, name='fetch_search_results'),
]