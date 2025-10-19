from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path("detail/<int:pk>/", views.detail, name='detail'),
    path("recent/", views.recent, name='recent'),
]
