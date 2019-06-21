from django.contrib import admin
from .models import Books, Tag, Type
# Register your models here.


class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'downloads', 'slug', 'uploader')
    search_fields = ['title', 'author']


admin.site.register(Books, BooksAdmin)
admin.site.register(Type)
admin.site.register(Tag)