from django.views import View
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import get_object_or_404, render
from .models import Subscriber

class UnsubscribeView(View):

    def get(self, request, token):

        subscriber = get_object_or_404(Subscriber, token=token)
        subscriber.is_active = False
        subscriber.save()

        return JsonResponse({
            "message": "You have unsubscribed."
        })

class ConfirmSubscriptionView(View):

    def get(self, request, token):

        subscriber = get_object_or_404(Subscriber, token=token)

        subscriber.is_active = True
        subscriber.save()

        # return JsonResponse({
        #     "message": "Subscription confirmed!"
        # })
        return render(request, 'newsletter/subscription_done.html', {'title':'Subscription done'})

class SubscribeView(View):

    def post(self, request):

        email = request.POST.get("email")

        if not email:
            return JsonResponse({"message": "Email required"}, status=400)

        subscriber, created = Subscriber.objects.get_or_create(email=email)

        if subscriber.is_active:
            return JsonResponse({"message": "You are already subscribed."})

        confirmation_link = f"{settings.SITE_URL}/newsletter/confirm/{subscriber.token}/"

        send_mail(
            "Confirm your subscription",
            f"Click the link to confirm: {confirmation_link}",
            settings.DEFAULT_FROM_EMAIL,
            [email]
        )

        return JsonResponse({
            "message": "Check your email to confirm subscription."
        })