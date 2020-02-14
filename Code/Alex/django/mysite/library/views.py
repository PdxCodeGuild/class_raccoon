from django.shortcuts import render



def index(request):
    authors = Author.objects.order_by('date_published')
    context = {
        'authors': authors
    }
    return render(request, 'library/index.html', context)