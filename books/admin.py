from django.contrib import admin
from .models import Books, Faculty, Type, Level
# Register your models here.
admin.site.register(Books)
admin.site.register(Faculty)
admin.site.register(Type)
admin.site.register(Level)
