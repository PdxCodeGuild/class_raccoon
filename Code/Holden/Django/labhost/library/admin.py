from django.contrib import admin
from .models import Book, Author, BookCheckout, Checkout

class AuthorshipInline(admin.TabularInline):
    model = Book.authors.through

class AuthorAdmin(admin.ModelAdmin):
    model = Author
    inlines = [
        AuthorshipInline,
    ]


admin.site.register(Checkout)
admin.site.register(BookCheckout)
admin.site.register(Book)
admin.site.register(Author, AuthorAdmin)
