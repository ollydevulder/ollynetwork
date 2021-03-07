from django.urls import path

from . import views

urlpatterns = [
    path('birthday/<str:person>', views.birthday, name='birthday'),
]
