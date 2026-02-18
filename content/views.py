from django.http import JsonResponse
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
        context['related_posts'] = Post.objects.filter(post_type=self.object.post_type)
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
        context['related_posts'] = Post.objects.filter(post_type=self.object.post_type)
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
        context['related_posts'] = Post.objects.filter(post_type=self.object.post_type)
        return context

class NewsView(ListView):
    template_name = 'content/news.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'News'
        return context
    
def fetch_leaks(request):
    posts = []
    p_results = Post.objects.filter(post_type='leaks')
    for p_result in p_results:
        result = {
            'id': p_result.id,
            'title': p_result.title,
            'thumbnail': p_result.thumbnail.url,
            'content': p_result.content,
            'post_type': p_result.post_type,
            'slug': p_result.slug,
        }
        posts.append(result)
    return JsonResponse({'my_response':'This is the response.','posts':posts})
    
def fetch_news(request):
    posts = []
    p_results = Post.objects.filter(post_type='news')
    for p_result in p_results:
        result = {
            'id': p_result.id,
            'title': p_result.title,
            'thumbnail': p_result.thumbnail.url,
            'content': p_result.content,
            'post_type': p_result.post_type,
            'slug': p_result.slug,
        }
        posts.append(result)
    return JsonResponse({'my_response':'This is the response.','posts':posts})
    
def fetch_did_you_know(request):
    posts = []
    p_results = Post.objects.filter(post_type='did_you_know')
    for p_result in p_results:
        result = {
            'id': p_result.id,
            'title': p_result.title,
            'thumbnail': p_result.thumbnail.url,
            'content': p_result.content,
            'post_type': p_result.post_type,
            'slug': p_result.slug,
        }
        posts.append(result)
    return JsonResponse({'my_response':'This is the response.','posts':posts})