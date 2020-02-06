from django.contrib import admin

from .models import BlogPostType, BlogPost


admin.site.register(BlogPostType)
admin.site.register(BlogPost)


