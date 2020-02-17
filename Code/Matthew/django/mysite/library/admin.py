from django.contrib import admin

from .models import Book, Author


class AuthorshipInline(admin.TabularInline):
    model = Book.authors.through

class AuthorAdmin(admin.ModelAdmin):
    model = Author
    inlines = [
        AuthorshipInline,
    ]


admin.site.register(Book)
admin.site.register(Author, AuthorAdmin)
