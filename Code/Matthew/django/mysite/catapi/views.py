from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
import requests
import json
import random
from .models import CatImage


def index(request):
    cat_image = random.choice(CatImage.objects.all())

    context = {
        'cat_image': cat_image,
    }
    return render(request, 'catapi/index.html', context)

def detail(request, cat_image_id):
    cat_image = CatImage.objects.get(id=cat_image_id)
    context = {
        'cat_image': cat_image,
    }
    return render(request, 'catapi/index.html', context)


def favorite(request, cat_image_id):
    cat_image = CatImage.objects.get(id=cat_image_id)
    cat_image.favorite = not cat_image.favorite
    cat_image.save()
    return HttpResponseRedirect(reverse('catapi:detail', args=(cat_image.id,)))

def favorited(request):
    cat_images = CatImage.objects.filter(favorite=True)
    context = {
        'cat_images': cat_images
    }
    return render(request, 'catapi/favorited.html', context)


def index2(request):

    response = requests.get('https://api.thecatapi.com/v1/images/search')
    data = json.loads(response.text)
    url = data[0]['url']

    context = {
        'url': url
    }
    return render(request, 'catapi/index2.html', context)
