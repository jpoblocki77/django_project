from.django.urls import render
from . import views

urlpatters = [
    path(''), views.home, name='blog home')
]