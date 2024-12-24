from django.contrib import admin

from libraries.models import BookModel


@admin.register(BookModel)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'publisher')
    search_fields = ('id', 'author', 'publisher')

