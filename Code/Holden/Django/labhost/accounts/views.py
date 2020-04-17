from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def register(request):
    message = request.GET.get('message', '')
    next = request.GET.get('next', '')
    context = {
        'next': next,
        'message': message
    }
    return render(request, 'accounts/register.html', context)

def save_user(request):
    if 'user_id' not in request.POST:
        next = request.GET.get('next', '')
        try:
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            password2 = request.POST['pass_check']
        except KeyError:
            return redirect(reverse('accounts:register') + '?message=invalid')
        if 150 < len(username) or len(username) < 6 or password != password2:
            return redirect(reverse('accounts:register') + '?message=invalid')


        if User.objects.filter(username=username):
            return redirect(reverse('accounts:register') + '?message=user_exists')
        user = User.objects.create_user(username, email, password)
        login(request, user)
        if next != '':
            return redirect(next)
        return redirect(reverse('accounts:home'))
    else:
        pass

def login_page(request):
    message = request.GET.get('message', '')
    next = request.GET.get('next', '')
    context = {
        'next': next,
        'message': message
    }
    return render(request, 'accounts/login.html', context)

def login_user(request):
    try:
        next = request.POST['next']
        username = request.POST['username']
        password = request.POST['password']
    except KeyError:
        return redirect('http://tehurn.com/not')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        if next != '':
            return redirect(next)
        return redirect(reverse('accounts:home'))
    if next == '':
        return redirect(reverse('accounts:login') + '?message=failure')
    return redirect(reverse('accounts:login') + '?message=failure&next='+next)

def logout_user(request):
    logout(request)
    return redirect(reverse('accounts:login') + '?message=loggedout')

@login_required
def user_home(request):
    return render(request, 'accounts/home.html')

@login_required
def user_profile(request):
    return render(request, 'accounts/user_profile.html')
