from django.db import models

# Create your models here.


class RestaurantTable(models.Model):
    number = models.IntegerField(unique=True)
    num_of_seats = models.IntegerField()

    class Meta:
        db_table = 'restaurant_tables'

    def __str__(self):
        return str(self.number)
