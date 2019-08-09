from django.contrib import admin
from django.urls import path, include
from books import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('ice/', admin.site.urls),
    path('', views.home, name='home'),
    path('documents/', include('books.urls')),
    path('accounts/', include('accounts.urls')),
    path('auth/', include('social_django.urls'), name='social')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
