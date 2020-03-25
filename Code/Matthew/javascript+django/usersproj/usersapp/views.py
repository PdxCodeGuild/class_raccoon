from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def index(request):
  return render(request, 'usersapp/index.html')


def register(request):
  return render(request, 'usersapp/register.html', {})


@login_required
def protected(request):
  return render(request, 'usersapp/protected.html', {})

def register_user(request):
  user = User.objects.create_user(request.POST['username'],
                                  request.POST['email'],
                                  request.POST['password'])
  user.image = request.FILES['image']
  user.save()

  login(request, user)
  # print(request.POST)
  # print(request.FILES)
  return HttpResponseRedirect(reverse('usersapp:protected'))
