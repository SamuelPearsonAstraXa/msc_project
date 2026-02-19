from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('logout/', views.logout_view, name='user-logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    # path('user-login/', views.UserLoginView.as_view(), name='user-login'),
    # path('<str:slug>/edit/', views.EditUserProfileView.as_view(), name='edit-user-profile'),
    # path('<str:slug>/', views.UserProfileView.as_view(), name='user-profile'),
]