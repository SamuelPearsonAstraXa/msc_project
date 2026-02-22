from django import forms
from .models import Tag, Post

class CreateTagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['slug', 'thumbnail', 'post_type',]

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['slug', 'thumbnail',]