from django.contrib import admin

from .models import Author, Publisher, Book


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['last_name', 'first_name']#pole wyszukiwania
    ordering = ['last_name'] #sortowanie po nazwisku


class BookAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'author', 'isbn', 'publisher']


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register([Publisher, ])
