from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
import json
import django.contrib.auth


def index(request):
  return render(request, 'usersajax/index.html', {})

def login(request):
  data = json.loads(request.body)
  username = data['username']
  password = data['password']
  user = django.contrib.auth.authenticate(request, username=username, password=password)
  if user is not None:
    django.contrib.auth.login(request, user)
    return HttpResponse('success')
  return HttpResponse('fail')

@login_required
def logout(request):
  django.contrib.auth.logout(request)
  return HttpResponse('ok')

@login_required
def get_user_data(request):
  return JsonResponse({
    'fruits': [
      'apples', 'bananas', 'pears', 'avocados'
    ]
  })