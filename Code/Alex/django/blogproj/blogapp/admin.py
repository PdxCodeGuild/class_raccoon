from django.contrib import admin

from .models import BlogPostType, BlogPost
# Register your models here



admin.site.register(BlogPostType)
admin.site.register(BlogPost)