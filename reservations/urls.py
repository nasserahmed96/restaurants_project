from django.urls import path
from .views import create_reservation, get_time_slots

urlpatterns = [
    path('create_reservation', create_reservation, name='create_reservation'),
    path('get_time_slots', get_time_slots, name='get_time_slots')
]