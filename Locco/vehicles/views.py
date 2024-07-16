from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

class LoginView(auth_views.LoginView):
    template_name = 'vehicles/templates/login.html'

class LogoutView(auth_views.LogoutView):
    template_name = 'vehicles/templates/logout.html'

class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'vehicles/templates/register.html'

def home(request):
    return render(request, 'vehicles/templates/home.html')  # Add a template for home
