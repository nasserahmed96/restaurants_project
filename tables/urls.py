from django.urls import path
from .views import create_table, view_tables, delete_table

urlpatterns = [
    path('create_table', create_table, name='create_table'),
    path('view_tables', view_tables, name='view_tables'),
    path('delete_table/<int:table_id>', delete_table, name='delete_table')
]