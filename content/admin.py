from django.contrib import admin
from .models import Post, Tag, Content, ContentBlock

class ContentBlockInline(admin.TabularInline):
    model = ContentBlock
    extra = 1
    
admin.site.register(Tag)
admin.site.register(Post)

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    inlines = [ContentBlockInline]
    prepopulated_fields = {'slug':('title',)}