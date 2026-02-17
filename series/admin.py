from django.contrib import admin
from .models import Series, Season, Episode

admin.site.register(Episode)
admin.site.register(Season)
admin.site.register(Series)