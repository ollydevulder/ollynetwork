from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('about.urls'), name='about'),
    path('', include('tools.urls'), name='tools'),
    path('admin/', admin.site.urls, name='admin'),
]
