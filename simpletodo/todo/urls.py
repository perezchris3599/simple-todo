from django.urls import path

from todo import views

urlpatterns = [
    path('', views.todos, name='todos'),
]