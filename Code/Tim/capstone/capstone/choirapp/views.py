from django.shortcuts import render, HttpResponse
import django.contrib.auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
import datetime
import json
from .models import Composition, Librarian, Composer, Rehearsal

def index(request):
    return render(request, 'index.html')

def make_list(request):
    current = Composition.objects.filter(turn_in_date__isnull = False)
    today = datetime.date.today()
    data = []
    for piece in current:
        data.append({
            'composer': piece.comp_last.comp_last,
            'piece': piece.title,
            'turn_in_date': piece.turn_in_date,
            'choristers': piece.choristers
        })

def in_folder(request):
    current = Composition.objects.filter(turn_in_date__isnull = False)
    today = datetime.date.today()
    data = []
    current_list = []
    for piece in current:
        data.append({
            'id': piece.id,
            'composer': piece.comp_last.comp_last,
            'piece': piece.title,
            'turn_in_date': piece.turn_in_date,
            'choristers': piece.choristers
        })
    for i in range(len(data)):
        if data[i]['turn_in_date'] >= today:
            current_list.append({
            'id': data[i]['id'],
            'composer': data[i]['composer'],
            'piece': data[i]['piece'],
            'turn_in_date': data[i]['turn_in_date'].strftime('%m-%d'),
            'edit_turn_in_date': data[i]['turn_in_date'],
            'choristers': data[i]['choristers']
            })
    return JsonResponse({'compositions': current_list})

def turn_in(request):
    current = Composition.objects.filter(turn_in_date__isnull = False)
    print(current)
    today = datetime.date.today()
    offset = (today.weekday() - 6)
    coming_sunday = today - datetime.timedelta(days=offset)
    data = []
    turn_in_list = []
    for piece in current:
        data.append({
            'composer': piece.comp_last.comp_last,
            'piece': piece.title,
            'turn_in_date': piece.turn_in_date,
            'choristers': piece.choristers
        })
    for i in range(len(data)):
        if data[i]['turn_in_date'] >= today and data[i]['turn_in_date'] <= coming_sunday:
            turn_in_list.append({
            'composer': data[i]['composer'],
            'piece': data[i]['piece'],
            'turn_in_date': data[i]['turn_in_date'],
            'choristers': data[i]['choristers']
            })
    return JsonResponse({'turn_ins': turn_in_list})

def this_season(request):
    current = Composition.objects.filter(turn_in_date__isnull = False)
    today = datetime.date.today()
    data = []
    late = []
    for piece in current:
        data.append({
            'composer': piece.comp_last.comp_last,
            'piece': piece.title,
            'turn_in_date': piece.turn_in_date,
            'choristers': piece.choristers
        })
    for i in range(len(data)):
        if data[i]['turn_in_date'] < today:
            late.append({
            'composer': data[i]['composer'],
            'piece': data[i]['piece'],
            'turn_in_date': data[i]['turn_in_date'],
            'choristers': data[i]['choristers']
            })

    return JsonResponse({'late_stuffs': late})

def lib_login(request):
    data = json.loads(request.body)
    password = data['password']
    user = django.contrib.auth.authenticate(request, username='Librarian', password=password)
    if user is not None:
      django.contrib.auth.login(request, user)
      return HttpResponse('success')
    return HttpResponse('fail')


@login_required
def save_piece(request):

    data = json.loads(request.body)
    catalog = data['catalog']
    comp_last = data['comp_last'].capitalize()
    comp_first = data['comp_first']
    title = data['title'].capitalize()
    voicing = data['voicing']
    notes = data['notes']
    location = data['location']
    copies = data['copies']
    choristers = str(data['choristers']).capitalize()
    turnin = data['turnin']

    if turnin == '':
        turnin = None

    if title == '':
        return HttpResponse('not ok')

    composer, created = Composer.objects.get_or_create(comp_last=comp_last, comp_first=comp_first)

    composition = Composition(cat_num=catalog, comp_last=composer, title=title, copies=copies, voicing=voicing, spec_notes=notes, location=location, choristers=choristers, turn_in_date=turnin)

    composition.save()

    return HttpResponse('ok')

@login_required
def edit_due(request):
    data = json.loads(request.body)
    composition = Composition.objects.filter(id=data['id'])
    composition.update(turn_in_date=data['new_due'])
    return HttpResponse('edit_due function response')


@login_required
def rehearsal(request):
    Rehearsal.objects.all().delete()
    data = json.loads(request.body)
    notes = data['notes']
    pieces = ''

    for i in range(len(data['pieces'])):
        if isinstance(data['pieces'][i]['piece'], str):
            pieces += data['pieces'][i]['piece']+', '


    rehearsal = Rehearsal(pieces=pieces, notes=notes)
    rehearsal.save()
    pieces = pieces.split(',')

    return JsonResponse({'rehearsal': pieces})

def schedule(request):
    data = Rehearsal.objects.all()
    note = data[0].notes
    schedule = []
    pieces = data[0].pieces.split(',')


    for piece in pieces:
        if piece != ' ':
            schedule.append({
            'pieces': piece
            })

    return JsonResponse({'schedule': schedule, 'note': note})

def set_folder(request):
    data = json.loads(request.body)
    search = Composition.objects.filter(title__icontains=data['search'])
    dump = []
    results = []

    for piece in search:
        dump.append({
            'id': piece.id,
            'composer': piece.comp_last.comp_last,
            'piece': piece.title,
            'turn_in_date': piece.turn_in_date,
            'choristers': piece.choristers
    })
    for i in range(len(dump)):
        results.append({
        'id': dump[i]['id'],
        'composer': dump[i]['composer'],
        'piece': dump[i]['piece'],
        'turn_in_date': dump[i]['turn_in_date'],
        'choristers': dump[i]['choristers']
        })
    print(results)
    return JsonResponse({'results': results})
