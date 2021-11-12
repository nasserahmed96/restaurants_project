from django.urls import path
from .views import create_table

urlpatterns = [
    path('create_table', create_table, name='create_table'),
]