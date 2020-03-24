from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Word
import json

def index(request):
  # return render(request, 'search/index.html')
  return render(request, 'search/index_vuetify.html')


def suggestions(request):
  words = Word.objects.filter(word__icontains=request.GET['text'])[:20]
  # words = [{'word': word.word, 'definition': word.definition} for word in words]
  data = {'words': []}
  for word in words:
    data['words'].append({
      'id': word.id,
      'word': word.word,
      'definition': word.definition,
      'counter': word.counter
    })
  return JsonResponse(data)

def increment_counter(request):
  data = json.loads(request.body)
  word_id = data['word_id']
  word = Word.objects.get(id=word_id)
  word.counter += 1
  word.save()
  return HttpResponse('ok')
