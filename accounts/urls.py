from django.urls import path, include
from . import views


urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('resetpassword/', views.rPassword, name='password_reset')
]