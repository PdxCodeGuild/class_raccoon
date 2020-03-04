


from django.core.management.base import BaseCommand
from blogapp.models import BlogPost
from django.utils import timezone
import json
import requests

class Command(BaseCommand):
    def handle(self, *args, **options):
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        print(response.text)
        posts = json.loads(response.text)
        for post in posts:
            blog_post = BlogPost(title=post['title'], body=post['body'], created_date=timezone.now())
            blog_post.save()