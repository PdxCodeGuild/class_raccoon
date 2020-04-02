


from django.core.management.base import BaseCommand
from search.models import Word
import json

class Command(BaseCommand):
  def handle(self, *args, **options):
    with open('./search/management/commands/dictionary.json', 'r') as file:
      data = file.read()
    data = json.loads(data)
    Word.objects.all().delete()
    i = 0
    for word, definition in data.items():
      word_model = Word(word=word, definition=definition)
      word_model.save()
      if i%1000 == 0:
        print(word + ' ' + str(round(i/len(data)*100,2))+'%')
      i += 1






