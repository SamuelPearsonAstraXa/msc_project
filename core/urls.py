from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('fetch_posts/', views.fetch_posts, name='fetch-data'),
    path('contact/', views.ContactUsView.as_view(), name='contact'),
    path('message-sent/', views.MessageSentView.as_view(), name='msg-sent'),
    path('messages/', views.MessagesView.as_view(), name='messages'),
    path('messages/<str:id>/', views.MessageDetailView.as_view(), name='message'),
    path('messages/<str:id>/delete/', views.DeleteMessageView.as_view(), name='delete-message'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('fetch_search_results/', views.fetch_search_results, name='fetch_search_results'),
]