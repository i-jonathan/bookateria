from django.contrib import admin
from django.urls import path, include
from books import views

urlpatterns = [
    path('ice/', admin.site.urls),
    path('', views.home, name='home'),
    path('books/', include('books.urls')),
    path('accounts/', include('accounts.urls')),
]
