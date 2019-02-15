from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('reset-password/', auth_views.PasswordResetView.as_view(
        template_name='accounts/reset-password.html'),
         name='password_reset'),
]