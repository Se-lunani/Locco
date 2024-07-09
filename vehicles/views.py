from django.shortcuts import render

# Create your views here.
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

class LoginView(auth_views.LoginView):
    template_name = 'vehicles/login.html'

class LogoutView(auth_views.LogoutView):
    template_name = 'vehicles/logout.html'

class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'vehicles/register.html'

