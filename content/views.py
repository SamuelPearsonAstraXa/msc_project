from django.shortcuts import render
from .models import Post
from django.views.generic import ListView

class DidYouKnowsView(ListView):
    template_name = 'content/did_you_know.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Did you know?'
        return context

class LeaksView(ListView):
    template_name = 'content/leaks.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Leaks'
        return context

class NewsView(ListView):
    template_name = 'content/news.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'News'
        return context