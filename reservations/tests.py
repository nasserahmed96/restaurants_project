import random
from django.test import TestCase
import datetime
from tables.models import RestaurantTable
from staff.models import User
from .models import Reservation
from django.conf import settings
# Create your tests here.


class ReservationTestCase(TestCase):
    def get_user_data(self):
        return {'password': 'secret', 'name': 'Nasser'}

    def generate_tables(self):
        tables = [RestaurantTable(number=n, num_of_seats=random.randint(1, 12)) for n in range(1, 25)]
        RestaurantTable.objects.bulk_create(tables)

    def get_reservation_data(self):
        return {'customer_name': 'Nasser',
                       'start_time': datetime.time(hour=13, minute=0),
                       'end_time': datetime.time(hour=14, minute=30),
                       'date': datetime.date(year=2021, month=11, day=15),
                       'employee': User.objects.create_user(**self.get_user_data()),
                       'num_of_customer_seats': 5}

    def get_reservation_table(self):
        reservation = self.get_reservation_data()
        table = RestaurantTable.objects.filter(num_of_seats__gte=reservation['num_of_seats'])

    def test_correct_working_hours(self):
        table = self.get_reservation_table()
        Reservation.objects.create(**self.get_reservation_data())

    def test_wrong_working_hours(self):
        reservation = self.get_reservation_data()
        reservation['start_time'] = datetime.time(hour=13, minute=0)
        reservation['end_time'] = datetime.time(hour=12, minute=45)
        Reservation.objects.create(**reservation)

    def test_wrong_num_of_seats(self):
        reservation = self.get_reservation_data()
        reservation['num_of_customer_seats'] = 7
        Reservation.objects.create(**reservation)


