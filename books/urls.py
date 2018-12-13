from django.urls import path
from . import views

urlpatterns = [
    path('addbook/', views.add, name='addbook'),
    path('<int:books_id>', views.detail, name='detail'),
    path('<int:books_id>/download', views.download, name='download'),
]
