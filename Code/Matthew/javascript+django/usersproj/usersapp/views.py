from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import User
from django.contrib.auth.decorators import login_required
import django.contrib.auth


def index(request):
  return render(request, 'usersapp/index.html')

@login_required
def protected(request):
  return render(request, 'usersapp/protected.html', {})


def register(request):
  # if 'message' in request.GET
  message = request.GET.get('message', '')
  return render(request, 'usersapp/register.html', {'message': message})

def register_user(request):

  username = request.POST['username']


  # try:
  #   User.objects.get(username=username)
  # except:

  # if User.objects.filter(username=username).first() is not None:
  # if User.objects.filter(username=username).count() > 0:
  if User.objects.filter(username=username).exists():
    return HttpResponseRedirect(reverse('usersapp:register')+'?message=already_taken')

  user = User.objects.create_user(request.POST['username'],
                                  request.POST['email'],
                                  request.POST['password'])
  user.image = request.FILES['image']
  user.save()

  django.contrib.auth.login(request, user)
  # print(request.POST)
  # print(request.FILES)
  return HttpResponseRedirect(reverse('usersapp:protected'))


def login(request):
  message = ''
  if request.method == 'POST': # form submission
    username = request.POST['username']
    password = request.POST['password']
    user = django.contrib.auth.authenticate(request, username=username, password=password)
    if user is not None:
      django.contrib.auth.login(request, user)
      return HttpResponseRedirect(reverse('usersapp:protected'))
    message = 'fail'
  return render(request, 'usersapp/login.html', {'message': message})


@login_required
def logout(request):
  django.contrib.auth.logout(request)
  return HttpResponseRedirect(reverse('usersapp:login'))

