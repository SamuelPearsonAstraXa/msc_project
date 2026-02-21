from django import forms
from .models import Movie, Actor, Genre

class CreateGenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']

class CreateActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = '__all__'
        exclude = ['slug', 'thumbnail',]

        widgets = {
            'birth_date': forms.DateInput(attrs={'type':'date'})
        }

class CreateMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        exclude = ['slug', 'thumbnail',]

        widgets = {
            'birth_date': forms.DateInput(attrs={'type':'date'}),
            'release_date': forms.DateInput(attrs={'type':'date'}),
        }