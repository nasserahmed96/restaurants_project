import datetime
from .models import Reservation

OPENING = datetime.time(hour=12, minute=0)
CLOSING = datetime.time(hour=23, minute=59)


def validate_working_hours(reservation_start_time, reservation_end_time):
    """"
    Check if the starting time and ending time for the reservation are in restaurant working hours
    """
    if reservation_start_time < reservation_end_time and reservation_start_time > OPENING and reservation_end_time < CLOSING:
        return True
    return False


def validate_reservations_overlapping(table_id, start_time, end_time, date):
    Reservation.objects.filter(table_id=table_id, date=date, start_time__gte=start_time, end_time__lte=end_time)


def validate_table_seats(table_num_of_seats, customer_required_seats):
    """
    Check if the required seats by the customer are less than or equal the table's seats
    """
    return True if table_num_of_seats >= customer_required_seats else False
