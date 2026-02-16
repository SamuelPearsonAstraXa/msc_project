from django.urls import path
from . import views

app_name = 'content'

urlpatterns = [
    path('did_you_know/', views.DidYouKnowsView.as_view(), name='did_you_know'),
    path('leaks/', views.LeaksView.as_view(), name='leaks'),
    path('news/', views.NewsView.as_view(), name='news'),
]