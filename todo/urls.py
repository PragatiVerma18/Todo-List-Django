from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add/', views.add, name='add'),
    path('delete/<todo_id>/',views.delete_todo, name='delete_todo'),
]