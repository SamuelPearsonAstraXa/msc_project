from django.db import models
from uuid import uuid4
from PIL import Image
from io import BytesIO
from django.urls import reverse
from django.conf import settings
from django.core.files.base import ContentFile
from django.utils.text import slugify
from accounts.models import CustomUser

class ContentBlock(models.Model):
    BLOCK_TYPES = [
        ('text', 'Text'),
        ('image', 'Image'),
        ('quote', 'Quote'),
    ]

    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    content = models.ForeignKey('Content', on_delete=models.CASCADE, related_name='blocks')
    type = models.CharField(choices=BLOCK_TYPES, max_length=30)

    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='content/block/images/', blank=True, null=True)

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return str(self.id)
    
    def save(self, *args, **kwargs):        
        super().save(*args, **kwargs)

        if self.image:
            img = Image.open(self.image)
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            img.thumbnail((720,720))
            buffer = BytesIO()
            img.save(buffer, format='JPEG', quality=85)
            buffer.seek(0)
            self.image.save(f"{self.id}-image.jpg", ContentFile(buffer.read()), save=False)

        super().save(update_fields=["image"])

class ContentCategory(models.TextChoices):
    STORIES = 'stories'
    FACTS = 'facts'
    LEAKS = 'leaks'

class Content(models.Model):
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    thumbnail = models.ImageField(upload_to='content/thumbnails', blank=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.CharField(max_length=30, null=True)
    title = models.CharField(max_length=255)
    is_trending = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    slug = models.SlugField(default='', blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.title) + "-" + str(uuid4())[:8]
        
        super().save(*args, **kwargs)

        if self.thumbnail:
            img = Image.open(self.thumbnail)
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            img.thumbnail((500,500))
            buffer = BytesIO()
            img.save(buffer, format='JPEG', quality=85)
            buffer.seek(0)
            self.thumbnail.save(f"{self.slug}-thumbnail.jpg", ContentFile(buffer.read()), save=False)

        super().save(update_fields=["thumbnail"])

    def get_absolute_url(self):
        return reverse('content:content', kwargs={'id':self.id})

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
            self.slug = slugify(self.title) + "-" + str(uuid4())[:8]
        
        super().save(*args, **kwargs)

        if self.featured_image:
            img = Image.open(self.featured_image)
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            img.thumbnail((500,500))
            buffer = BytesIO()
            img.save(buffer, format='JPEG', quality=85)
            buffer.seek(0)
            self.thumbnail.save(f"{self.slug}-thumbnail.jpg", ContentFile(buffer.read()), save=False)

        super().save(update_fields=["thumbnail"])