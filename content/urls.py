from django.urls import path
from . import views

app_name = 'content'

urlpatterns = [
    path('did_you_know/', views.DidYouKnowsView.as_view(), name='did_you_know'),
    path('did_you_know/<str:id>/', views.DidYouKnowDetailView.as_view(), name='did_you_know_detail'),
    path('leaks/', views.LeaksView.as_view(), name='leaks'),
    path('leaks/<str:id>/', views.LeakDetailView.as_view(), name='leak_detail'),
    path('news/', views.NewsView.as_view(), name='news'),
    path('news/<str:id>/', views.NewsDetailView.as_view(), name='news_detail'),
]