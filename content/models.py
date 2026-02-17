from django.db import models
from uuid import uuid4
from PIL import Image
from io import BytesIO
from django.conf import settings
from django.core.files.base import ContentFile
from django.utils.text import slugify

class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class PostType(models.TextChoices):
    NEWS = 'news'
    LEAK = 'leaks'
    DID_YOU_KNOW = 'did_you_know'
    BEHIND_SCENES = 'behind_scenes'

class Post(models.Model):
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=255)
    post_type = models.CharField(max_length=30, choices=PostType.choices)
    featured_image = models.ImageField(upload_to='posts/featured_images')
    thumbnail = models.ImageField(upload_to='posts/thumbnails', blank=True)
    content = models.TextField(blank=True, default='')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    views = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True, default='')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.id)
        if self.featured_image:
            img = Image.open(self.featured_image)
            img.thumbnail((500,500))
            buffer = BytesIO()
            img.save(buffer, format='JPEG', quality=100)
            buffer.seek(0)
            self.thumbnail = ContentFile(buffer.read(), name=f'{str(self.featured_image.name)}-{str(self.id)}-thumbnail')

        super().save(*args, **kwargs)