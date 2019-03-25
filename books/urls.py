from django.urls import path
from . import views

urlpatterns = [
    path('add-a-document/', views.add, name='add-document'),
    path('all/', views.view_all, name='all-documents'),
    path('search/', views.search, name='search'),
    path('books/', views.books_view, name='books_view'),
    path('notes/', views.notes_view, name='notes_view'),
    path('questions/', views.question_view, name='question_view'),

]

urlpatterns += [
    path('<slug:slug>/', views.detail, name='detail'),
    path('<slug:slug>/download', views.download, name='download'),
]