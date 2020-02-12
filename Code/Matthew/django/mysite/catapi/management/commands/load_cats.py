



from django.core.management.base import BaseCommand
import json
import requests
from catapi.models import CatImage

class Command(BaseCommand):
    def handle(self, *args, **options):
        num_cats = 1000
        for i in range(num_cats):
            response = requests.get('https://api.thecatapi.com/v1/images/search')
            data = json.loads(response.text)
            cat_api_id = data[0]['id']
            url = data[0]['url']

            # if CatImage.objects.get(url=url) is None:
            if not CatImage.objects.filter(url=url).exists():
                cat_image = CatImage(cat_api_id=cat_api_id, url=url)
                cat_image.save()

            print(str(round(i/num_cats*100, 2))+'%')


