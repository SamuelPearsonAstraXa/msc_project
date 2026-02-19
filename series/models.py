from django.db import models
from movies.models import Actor
from accounts.models import CustomUser
from uuid import uuid4
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from django.utils.text import slugify

class Series(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')
    poster = models.ImageField(upload_to='series/poster',)
    thumbnail = models.ImageField(upload_to='series/thumbnails', blank=True, null=True)
    release_date = models.DateField()
    season_count = models.PositiveIntegerField(default=1)
    cast = models.ManyToManyField(CustomUser, blank=True)
    slug = models.SlugField(default='', unique=True, editable=False, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.title) + "-" + str(uuid4())[:8]
        
        super().save(*args, **kwargs)

        if self.poster:
            img = Image.open(self.poster)
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            img.thumbnail((500,500))
            buffer = BytesIO()
            img.save(buffer, format='JPEG', quality=85)
            buffer.seek(0)
            self.thumbnail.save(f"{self.slug}-thumbnail.jpg", ContentFile(buffer.read()), save=False)

        super().save(update_fields=["thumbnail"])

class Season(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    number = models.PositiveIntegerField()
    slug = models.SlugField(default='', unique=True, editable=False, blank=True)

    def __str__(self):
        return f'Season for {self.series.title}'

    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.series.title) + "-" + str(uuid4())[:8]
        super().save(*args, **kwargs)

class Episode(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=255)
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='episodes')
    episode_number = models.PositiveIntegerField()
    description = models.TextField(blank=True, default='')
    slug = models.SlugField(default='', unique=True, editable=False, blank=True)

    def __str__(self):
        return f'{self.season.series.title} - {self.title}'

    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.title) + "-" + str(uuid4())[:8]
        super().save(*args, **kwargs)