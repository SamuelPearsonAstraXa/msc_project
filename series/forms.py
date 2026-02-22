from django import forms
from .models import Series, Season, Episode

class CreateEpisodeForm(forms.ModelForm):
    class Meta:
        model = Episode
        fields = '__all__'
        exclude = ['slug', 'thumbnail',]

class CreateSeasonForm(forms.ModelForm):
    class Meta:
        model = Season
        fields = '__all__'
        exclude = ['slug', 'thumbnail',]

class UpdateSeriesForm(forms.ModelForm):
    class Meta:
        model = Series
        fields = '__all__'
        exclude = ['slug', 'thumbnail', 'post_type',]

        widgets = {
            'release_date': forms.DateInput(attrs={'type':'date'})
        }

class CreateSeriesForm(forms.ModelForm):
    class Meta:
        model = Series
        fields = '__all__'
        exclude = ['slug', 'thumbnail',]

        widgets = {
            'release_date': forms.DateInput(attrs={'type':'date'})
        }