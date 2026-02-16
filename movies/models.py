from django.db import models
from uuid import uuid4
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from django.utils.text import slugify

class Genre(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    slug = models.SlugField(default='', unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.id)
        super().save(*args, **kwargs)

class Actor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, default='')
    birth_date = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='actors/')
    thumbnail = models.ImageField(upload_to='actors/thumbnails', blank=True, null=True)
    slug = models.SlugField(default='', unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.id)
        if self.photo:
            img = Image.open(self.photo)
            img.thumbnail((500,500))
            buffer = BytesIO()
            img.save(buffer, format='JPEG', quality=100)
            buffer.seek(0)
            self.thumbnail = ContentFile(buffer.read(), name=f'{str(self.photo.name)}-{str(self.id)}-thumbnail')

        super().save(*args, **kwargs)

class Movie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=500)
    release_date = models.DateField()
    poster = models.ImageField(upload_to='movies/posters')
    thumbnail = models.ImageField(upload_to='movies/thumbnails', blank=True, null=True)
    description = models.TextField(default='', blank=True)
    duration = models.PositiveIntegerField(help_text='Duration in minutes')
    rating = models.FloatField(default=0)
    genres = models.ManyToManyField(Genre)
    cast = models.ManyToManyField(Actor, related_name='movie_casts')
    create_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default='', blank=True, unique=True)

    class Meta:
        ordering = ['-release_date']

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.id)
        if self.poster:
            img = Image.open(self.poster)
            img.thumbnail((500,500))
            buffer = BytesIO()
            img.save(buffer, format='JPEG', quality=100)
            buffer.seek(0)
            self.thumbnail = ContentFile(buffer.read(), name=f'{str(self.poster.name)}-{str(self.id)}-thumbnail')
         
        super().save(*args, **kwargs)