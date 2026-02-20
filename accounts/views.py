from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView, DetailView, UpdateView, View, TemplateView
from .forms import CustomUserCreationForm, CustomUserChangeForm
from content.models import Post, Tag
from series.models import Series, Season, Episode
from movies.models import Movie, Actor, Genre

class AdminDashboardView(PermissionRequiredMixin, TemplateView):
    template_name = 'accounts/admin-dashboard.html'
    permission_required = 'request.user.is_staff'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Dashboard'
        context['posts'] = Post.objects.all().order_by('-created_at')
        context['movies'] = Movie.objects.all().order_by('-create_date')
        context['series'] = Series.objects.all().order_by('-release_date')
        context['seasons'] = Season.objects.all()
        context['episodes'] = Episode.objects.all()
        context['actors'] = Actor.objects.all().order_by('name')
        context['genres'] = Genre.objects.all().order_by('name')
        context['tags'] = Tag.objects.all().order_by('name')
        
        return context


def logout_view(request):
    logout(request)
    return redirect('core:home')

class UserLoginView(LoginView):
    def form_valid(self, form):
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            login(self.request, form.get_user())
            success_url = self.get_success_url()
            return JsonResponse({'success': True, 'success_url': success_url})
        return super().form_valid(form)

    def form_invalid(self, form):
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'error': form.errors}, status=400)
        return super().form_invalid(form)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
        return context

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()

        if self.request.headers.get('X-Requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success':True, 'success_url':f'/accounts/login/'})

    def form_invalid(self, form):
        if self.request.headers.get('X-Requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success':False, 'error':form.errors}, status=400)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Register'

        return context