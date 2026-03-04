from uuid import uuid4
from django.db import models

class Subscriber(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    token = models.UUIDField(default=uuid4, unique=True, editable=False)
    subscription_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email