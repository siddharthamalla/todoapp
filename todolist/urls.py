from django.contrib import admin
from django.urls import path, include
from todolist import views
urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('tasks', views.tasks, name='tasks')
]