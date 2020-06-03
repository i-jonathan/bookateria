from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('', include('django.contrib.auth.urls'))
]
