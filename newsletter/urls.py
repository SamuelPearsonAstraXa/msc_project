from django.urls import path
from .views import SubscribeView, ConfirmSubscriptionView

urlpatterns = [
    path("subscribe/", SubscribeView.as_view(), name="subscribe"),
    path("confirm/<uuid:token>/", ConfirmSubscriptionView.as_view(), name="confirm_subscription"),
]