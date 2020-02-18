from django.contrib import admin
from .models import Author, Books, Book_checkout
# Register your models here.


admin.site.register(Author)
admin.site.register(Books)
admin.site.register(Book_checkout)