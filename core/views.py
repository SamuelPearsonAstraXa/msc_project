from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView, CreateView, ListView
from content.models import Post
from movies.models import Movie
from series.models import Series
from .forms import ContactForm
import random

class SearchView(ListView):
    template_name = 'core/search.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Search for posts'

        search_query = str(self.request.GET.get('search_query')).rstrip()
        if search_query:
            context['searched'] = True
            search_results = []

            movies = Movie.objects.filter(title__icontains=search_query)
            series = Series.objects.filter(title__icontains=search_query)
            posts = Post.objects.filter(title__icontains=search_query)

            for movie in movies:
                search_results.append(movie)
            for serie in series:
                search_results.append(serie)
            for post in posts:
                search_results.append(post)

            context['search_results'] = search_results
            if search_query != 'None' or search_query.strip() != ' ':
                context['search_query'] = search_query

            # for m_r in movies:
            #     movie = {
            #         'id':m_r.id,
            #         'title':m_r.title,
            #         'description':m_r.description,
            #         'thumbnail':m_r.thumbnail.url,
            #         'type':'movie',
            #     }
            #     search_results.append(movie)
            # for serie in series:
            #     s_r = {
            #         'id':serie.id,
            #         'title':serie.title,
            #         'description':serie.description,
            #         'thumbnail':serie.thumbnail.url,
            #         'type':'serie',
            #     }
            #     search_results.append(s_r)
            # for post in posts:
            #     p_r = {
            #         'id':post.id,
            #         'title':post.title,
            #         'description':post.description,
            #         'thumbnail':post.thumbnail.url,
            #         'type':'post',
            #     }
            #     search_results.append(p_r)

        return context

class ContactUsView(CreateView):
    form_class = ContactForm
    template_name = 'core/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contact us'
        return context

class HomeView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        context['featured_post'] = Post.objects.filter(is_featured=True)[0]
        return context
    
def fetch_search_results(request):
    search_results = []
    if request.method.GET.get('search_query'):
        search_query = request.method.GET.get('search_query')

        posts_results = Post.objects.filter(title__icontains=search_query).order_by('-title')
        movies_results = Movie.objects.filter(title__icontains=search_query).order_by('-title')
        series_results = Series.objects.filter(title__icontains=search_query).order_by('-title')
        for post_result in posts_results:
            result = {
                'id': post_result.id,
                'title': post_result.title,
                'thumbnail': post_result.thumbnail.url,
                'content': post_result.content,
                'post_type': post_result.post_type,
                'slug': post_result.slug,
            }
            search_results.append(result)
        for movie_result in movies_results:
            result = {
                'id': movie_result.id,
                'title': movie_result.title,
                'thumbnail': movie_result.thumbnail.url,
                'content': movie_result.description,
                'slug': movie_result.slug,
            }
            search_results.append(result)
        for series_result in series_results:
            result = {
                'id': series_result.id,
                'title': series_result.title,
                'thumbnail': series_result.thumbnail.url,
                'content': series_result.description,
                'slug': series_result.slug,
            }
            search_results.append(result)
    
    return JsonResponse({'my_response':'This is the response.','search_results':sorted(search_results, key='id')})
    
def fetch_posts(request):
    posts = []
    p_results = Post.objects.all()
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