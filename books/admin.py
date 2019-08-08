from django.contrib import admin
from .models import Document, Tag, Type
# Register your models here.


class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'downloads', 'slug', 'uploader')
    search_fields = ['title', 'author']


admin.site.register(Document, BooksAdmin)
admin.site.register(Type)
admin.site.register(Tag)