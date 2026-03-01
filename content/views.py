import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, View
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, UserPassesTestMixin
from django.db import transaction
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .models import Post, Content, ContentBlock
from .forms import CreatePostForm, CreateTagForm, UpdatePostForm

class CreateContentView(LoginRequiredMixin, UserPassesTestMixin, View):

    def test_func(self):
        return self.request.user.is_staff

    def get(self, request):
        return render(request, 'content/create_content.html', {
            'title': 'Create Content'
        })

    def post(self, request):

        title = request.POST.get("title")
        category = request.POST.get("category")
        thumbnail = request.FILES.get("thumbnail")

        if not title:
            return JsonResponse({"error": "Title required"}, status=400)

        try:
            with transaction.atomic():

                content = Content.objects.create(
                    title=title,
                    category=category,
                    thumbnail=thumbnail,
                    author=request.user
                )

                index = 0
                while True:

                    block_type = request.POST.get(f"blocks[{index}][type]")

                    if block_type is None:
                        break

                    ContentBlock.objects.create(
                        content=content,
                        type=block_type,
                        text=request.POST.get(f"blocks[{index}][text]"),
                        image=request.FILES.get(f"blocks[{index}][image]"),
                        order=index
                    )

                    index += 1

            return JsonResponse({
                "success": True,
                "success_url": content.get_absolute_url()
            })

        except Exception as e:
            return JsonResponse({
                "error": str(e)
            }, status=400)

class ContentDetail(DetailView):
    template_name = 'content/content.html'
    model = Content
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Content'
        return context

class ContentListView(ListView):
    template_name = 'content/contents.html'
    model = Content
    context_object_name = 'contents'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contents'
        return context

class CreateTagView(PermissionRequiredMixin, CreateView):
    permission_required = 'request.user.is_staff'
    permission_denied_message = 'Oh, sorry fan. Nice try!'
    form_class = CreateTagForm
    template_name = 'content/create_tag.html'
    success_url = '/accounts/admin-dashboard/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create tag'
        return context
    
class DeleteFact(PermissionRequiredMixin, DeleteView):
    permission_required = 'request.user.is_staff'
    permission_denied_message = 'Oh, sorry fan. Nice try!'
    template_name = 'content/delete_fact.html'
    model = Content
    context_object_name = 'post'
    pk_url_kwarg = 'id'
    success_url = '/content/facts/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Delete {self.object.title}'
        return context
    
class DeleteLeakView(PermissionRequiredMixin, DeleteView):
    permission_required = 'request.user.is_staff'
    permission_denied_message = 'Oh, sorry fan. Nice try!'
    template_name = 'content/delete_leak.html'
    model = Content
    context_object_name = 'post'
    pk_url_kwarg = 'id'
    success_url = '/content/leaks/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Delete {self.object.title}'
        return context
    
class DeleteStoryView(PermissionRequiredMixin, DeleteView):
    permission_required = 'request.user.is_staff'
    permission_denied_message = 'Oh, sorry fan. Nice try!'
    template_name = 'content/delete_story.html'
    model = Content
    context_object_name = 'post'
    pk_url_kwarg = 'id'
    success_url = '/content/stories/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Delete {self.object.title}'
        return context

class UpdatePostView(PermissionRequiredMixin, UpdateView):
    permission_required = 'request.user.is_staff'
    permission_denied_message = 'Oh, sorry fan. Nice try!'
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

class CreatePostView(PermissionRequiredMixin, CreateView):
    permission_required = 'request.user.is_staff'
    permission_denied_message = 'Oh, sorry fan. Nice try!'
    form_class = CreatePostForm
    template_name = 'content/create_post.html'
    success_url = '/accounts/admin-dashboard/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create post'
        return context

class FactDetailView(DetailView):
    template_name = 'content/fact_detail.html'
    model = Content
    context_object_name = 'post'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Did you know?'
        context['related_posts'] = Content.objects.filter(category=self.object.category)
        return context

class FactsView(ListView):
    template_name = 'content/facts.html'
    model = Content

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Facts'
        return context
    
class LeakDetailView(DetailView):
    template_name = 'content/leak_detail.html'
    model = Content
    context_object_name = 'post'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Leak'
        context['related_posts'] = Content.objects.filter(category=self.object.category)
        return context

class LeaksView(ListView):
    template_name = 'content/leaks.html'
    model = Content

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Leaks'
        return context
    
class StoryDetailView(DetailView):
    template_name = 'content/story_detail.html'
    model = Content
    context_object_name = 'post'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        context['related_posts'] = Content.objects.filter(category=self.object.category)
        return context

class StoriesView(ListView):
    template_name = 'content/stories.html'
    model = Content

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Stories'
        return context
    
class PostsView(ListView):
    template_name = 'content/posts_list.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Stories'
        return context
    
def fetch_leaks(request):
    posts = []
    p_results = Content.objects.filter(category='leaks')
    for p_result in p_results:
        result = {
            'id': p_result.id,
            'title': p_result.title,
            'thumbnail': p_result.thumbnail.url,
            'category': p_result.category,
            'slug': p_result.slug,
        }
        posts.append(result)
    return JsonResponse({'my_response':'This is the response.','posts':posts})
    
def fetch_stories(request):
    posts = []
    p_results = Content.objects.filter(category='stories')
    for p_result in p_results:
        result = {
            'id': p_result.id,
            'title': p_result.title,
            'thumbnail': p_result.thumbnail.url,
            'category': p_result.category,
            'slug': p_result.slug,
        }
        posts.append(result)
    return JsonResponse({'my_response':'This is the response.','posts':posts})
    
def fetch_facts(request):
    posts = []
    p_results = Content.objects.filter(category='facts')
    for p_result in p_results:
        result = {
            'id': p_result.id,
            'title': p_result.title,
            'thumbnail': p_result.thumbnail.url,
            'category': p_result.category,
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