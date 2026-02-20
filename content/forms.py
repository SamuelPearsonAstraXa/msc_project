from django import forms
from .models import Tag, Post

class CreateTagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['slug', 'thumbnail',]