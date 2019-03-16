from django.urls import path
from . import views

urlpatterns = [
    path('addbook/', views.add, name='addbook'),
    path('all/', views.bookview, name='allbooks'),
    path('<slug:slug>/', views.detail, name='detail'),
    path('<slug:slug>/download', views.download, name='download'),
    path('search/', views.search, name='search')
]