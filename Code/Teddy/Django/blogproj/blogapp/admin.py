from django.contrib import admin
from .models import BlogPostType, BlogPost

# display blog post and post type on admin page
admin.site.register(BlogPostType)
admin.site.register(BlogPost)
