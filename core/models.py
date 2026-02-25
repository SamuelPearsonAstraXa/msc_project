from django.db import models
from uuid import uuid4

class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    sender_email = models.EmailField()
    title = models.CharField(default='', blank=True, max_length=500)
    content = models.TextField()
    recieved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.sender_email}'