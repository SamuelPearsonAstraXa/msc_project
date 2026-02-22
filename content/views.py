from django.http import JsonResponse
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .forms import CreatePostForm, CreateTagForm, UpdatePostForm

class CreateTagView(CreateView):
    form_class = CreateTagForm
    template_name = 'content/create_tag.html'
    success_url = '/accounts/admin-dashboard/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create tag'
        return context
    
class DeleteDidYouKnowView(DeleteView):
    template_name = 'content/delete_did_you_know.html'
    model = Post
    context_object_name = 'post'
    pk_url_kwarg = 'id'
    success_url = '/content/did_you_know/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Delete {self.object.title}'
        return context
    
class DeleteLeakView(DeleteView):
    template_name = 'content/delete_leak.html'
    model = Post
    context_object_name = 'post'
    pk_url_kwarg = 'id'
    success_url = '/content/leaks/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Delete {self.object.title}'
        return context
    
class DeleteNewsView(DeleteView):
    template_name = 'content/delete_news.html'
    model = Post
    context_object_name = 'post'
    pk_url_kwarg = 'id'
    success_url = '/content/news/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Delete {self.object.title}'
        return context

class UpdatePostView(UpdateView):
    form_class = CreatePostForm
    model = Post
    form_class = UpdatePostForm
    pk_url_kwarg = 'id'
    template_name = 'content/create_post.html'

    def get_success_url(self):
        if self.object.post_type == 'leaks':
           return f'/content/leaks/{self.object.id}/'
        elif self.object.post_type == 'news':
           return f'/content/news/{self.object.id}/'
        else:
           return f'/content/did_you_know/{self.object.id}'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Update {self.object.title}'
        return context

class CreatePostView(CreateView):
    form_class = CreatePostForm
    template_name = 'content/create_post.html'
    success_url = '/accounts/admin-dashboard/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create post'
        return context

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
    
class PostsView(ListView):
    template_name = 'content/posts_list.html'
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

def fetch_posts(request):
    posts = []
    p_results = Post.objects.all().order_by('-created_at')
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