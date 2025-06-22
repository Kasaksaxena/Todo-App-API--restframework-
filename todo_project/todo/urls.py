from django.urls import path
from .import views
from .authentication import CustomAuthToken

urlpatterns=[
    path('todos/',views.todo_list_create, name='todo_list_create'),
    path('todos/<uuid:uuid>/',views.todo_detail),
    path('login/',CustomAuthToken.as_view(),name='custom_token_auth')
]