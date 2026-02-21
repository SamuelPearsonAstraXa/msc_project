from django.urls import path
from . import views

app_name = 'content'

urlpatterns = [
    path('', views.PostsView.as_view(), name='home'),
    path('fetch_posts/', views.fetch_posts, name='fetch_posts'),
    path('create/', views.CreatePostView.as_view(), name='create-post'),
    path('create/tag/', views.CreateTagView.as_view(), name='create-tag'),
    path('did_you_know/', views.DidYouKnowsView.as_view(), name='did_you_know'),
    path('fetch_did_you_know/', views.fetch_did_you_know, name='fetch_did_you_know'),
    path('did_you_know/<str:id>/', views.DidYouKnowDetailView.as_view(), name='did_you_know_detail'),
    path('leaks/', views.LeaksView.as_view(), name='leaks'),
    path('fetch_leaks/', views.fetch_leaks, name='fetch_leaks'),
    path('leaks/<str:id>/', views.LeakDetailView.as_view(), name='leak_detail'),
    path('news/', views.NewsView.as_view(), name='news'),
    path('fetch_news/', views.fetch_news, name='fetch_news'),
    path('news/<str:id>/', views.NewsDetailView.as_view(), name='news_detail'),
]