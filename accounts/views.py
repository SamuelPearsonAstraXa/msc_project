from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, DetailView, UpdateView, View
from .forms import CustomUserCreationForm, CustomUserChangeForm


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