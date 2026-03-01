from django.urls import path
from . import views

app_name = 'content'

urlpatterns = [
    path('', views.PostsView.as_view(), name='home'),
    path('fetch_posts/', views.fetch_posts, name='fetch_posts'),
    path('create/', views.CreatePostView.as_view(), name='create-post'),
    path('add/', views.CreateContentView.as_view(), name='create-content'),
    path('create/tag/', views.CreateTagView.as_view(), name='create-tag'),
    
    path('facts/', views.FactsView.as_view(), name='facts'),
    path('fetch_facts/', views.fetch_facts, name='fetch_facts'),
    path('facts/<str:id>/', views.FactDetailView.as_view(), name='fact-detail'),
    path('facts/<str:id>/delete/', views.DeleteFact.as_view(), name='delete-fact'),
    path('facts/<str:id>/update/', views.UpdatePostView.as_view(), name='update-fact'),
    
    path('leaks/', views.LeaksView.as_view(), name='leaks'),
    path('fetch_leaks/', views.fetch_leaks, name='fetch_leaks'),
    path('leaks/<str:id>/', views.LeakDetailView.as_view(), name='leak-detail'),
    path('leaks/<str:id>/delete/', views.DeleteLeakView.as_view(), name='delete-leak'),
    path('leaks/<str:id>/update/', views.UpdatePostView.as_view(), name='update-leak'),
   
    path('stories/', views.StoriesView.as_view(), name='stories'),
    path('fetch_stories/', views.fetch_stories, name='fetch_stories'),
    path('stories/<str:id>/', views.StoryDetailView.as_view(), name='story-detail'),
    path('stories/<str:id>/delete/', views.DeleteStoryView.as_view(), name='delete-story'),
    path('stories/<str:id>/update/', views.UpdatePostView.as_view(), name='update-story'),

    path('contents/', views.ContentListView.as_view(), name='contents'),
    path('contents/add/', views.CreateContentView.as_view(), name='create-content'),
    path('contents/<str:id>/', views.ContentDetail.as_view(), name='content'),
]