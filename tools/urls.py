from django.urls import path

from . import views

urlpatterns = [
    path('!', views.short_set, name='short index'),
    path('!<str:url>', views.short, name='short'),
    path('birthday/<str:person>', views.birthday, name='birthday'),
]
