from django.test import TestCase
from .models import RestaurantTable


# Create your tests here.
class TablesTestCase(TestCase):
    def test_correct_seats_number(self):
        table = {'number': 1, 'num_of_seats': 1}
        RestaurantTable.objects.create(**table)

    def test_wrong_seats_number(self):
        table = {'number': 1, 'num_of_seats': 13}
        RestaurantTable.objects.create(**table)
