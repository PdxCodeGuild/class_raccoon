from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import django.contrib.auth
from .models import User


def index(request):
  return render(request, 'users/index.html')

def login_register(request):
  return render(request, 'users/login_register.html')

def public(request):
  return render(request, 'users/public.html')

@login_required
def protected(request):
  return render(request, 'users/protected.html')


def login(request):
  username = request.POST['username']
  password = request.POST['password']
  user = django.contrib.auth.authenticate(request, username=username, password=password)
  if user is None: # authenticiation failed, send them back to the login/register page
    return HttpResponseRedirect(reverse('users:login_register'))
  # authentication succeeded, send them to the protected page
  django.contrib.auth.login(request, user)
  return HttpResponseRedirect(reverse('users:protected'))

def register(request):
  username = request.POST['username']
  email = request.POST['email']
  password = request.POST['password']
  user = User.objects.create_user(username, email, password)
  django.contrib.auth.login(request, user)
  return HttpResponseRedirect(reverse('users:protected'))

def logout(request):
  django.contrib.auth.logout(request)
  return HttpResponseRedirect(reverse('users:index'))
