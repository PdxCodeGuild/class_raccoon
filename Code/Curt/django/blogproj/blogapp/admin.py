from django.contrib import admin

# Register your models here.
from .models import BlogPostType, BlogPost


admin.site.register(BlogPostType)
admin.site.register(BlogPost)