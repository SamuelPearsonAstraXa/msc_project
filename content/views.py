from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

class DidYouKnowDetailView(DetailView):
    template_name = 'content/did_you_know_detail.html'
    model = Post
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Did you know?'
        return context

class DidYouKnowsView(ListView):
    template_name = 'content/did_you_know.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Did you know?'
        return context
    
class LeakDetailView(DetailView):
    template_name = 'content/leak_detail.html'
    model = Post
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Leak'
        return context

class LeaksView(ListView):
    template_name = 'content/leaks.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Leaks'
        return context
    
class NewsDetailView(DetailView):
    template_name = 'content/news_detail.html'
    model = Post
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        return context

class NewsView(ListView):
    template_name = 'content/news.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'News'
        return context