''' what i did originally before i created a template to display '''
# from django.shortcuts import render
# from django.http import HttpResponse
#
# def index(request):
#   return HttpResponse('hello world!')


from django.shortcuts import render

def index(request):
    context = {
        'message': 'Hello World!'
    }
    return render(request, 'blogapp/index.html', context)