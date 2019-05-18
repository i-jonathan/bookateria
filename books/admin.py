from django.contrib import admin
from .models import Books, Tag, Type
# Register your models here.
admin.site.register(Books)
admin.site.register(Type)
admin.site.register(Tag)