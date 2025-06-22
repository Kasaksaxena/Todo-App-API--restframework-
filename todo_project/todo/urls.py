from django.urls import path
from .import views

urlpatterns=[
    path('todos/',views.todo_list_create, name='todo_list_create'),
    path('todos/<uuid:uuid>/',views.todo_detail),
]