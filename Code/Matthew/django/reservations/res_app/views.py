from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import datetime
import json

from .models import Restaurant, Reservation
# Create your views here.
def index(request):
    return render(request, "res_app/index.html")

def get_restaurants(request):
    restaurants = Restaurant.objects.order_by('name')
    data = []
    for restaurant in restaurants:
        data.append({
            'id': restaurant.id,
            'name': restaurant.name,
            'address': restaurant.address,
            'tables': restaurant.tables
        })
    return JsonResponse({'restaurants': data})

def save_reservation(request):
    data = json.loads(request.body)
    party_name = data['party_name']
    party_size = data['party_size']
    restaurant_id = data['restaurant_id']
    time = data['time']
    date = data['date']
    # "date":"2020-03-10","time":"18:00"
    res_time = datetime.strptime(date + ' ' + time, '%Y-%m-%d %H:%M')
    save_res = Reservation(party_name=party_name, party_size=party_size, time=res_time, restaurant_id=restaurant_id)
    save_res.save()
    return HttpResponse("Okay, boss!")

def reservations(request):
    reservations = Reservation.objects.order_by('restaurant__name', '-time')
    data = []
    for res in reservations:
        data.append({
            'id': res.id,
            'party_name': res.party_name,
            'party_size': res.party_size,
            'time': res.time.strftime('%Y-%m-%d %H:%M'),
            'restaurant': res.restaurant.name
        })
    return JsonResponse({'reservations': data})