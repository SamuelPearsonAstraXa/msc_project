from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView, CreateView
from content.models import Post
from .forms import ContactForm

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