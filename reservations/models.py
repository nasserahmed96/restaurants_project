from django.db import models
from tables.models import RestaurantTable
from staff.models import User
# Create your models here.


class Reservation(models.Model):
    customer_name = models.CharField(max_length=45)
    num_of_customer_seats = models.IntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    date = models.DateField()
    table = models.ForeignKey(RestaurantTable, on_delete=models.DO_NOTHING)
    employee = models.ForeignKey(User, on_delete=models.DO_NOTHING)


    class Meta:
        db_table = 'reservations'

