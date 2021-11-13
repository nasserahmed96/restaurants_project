from django.db.models.signals import pre_save
from django.core.exceptions import ValidationError
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from .validators import *


@receiver(pre_save, sender=Reservation)
def validate_reservation(sender, instance, *args, **kwargs):
    if not validate_working_hours(instance.start_time, instance.end_time):
        raise ValidationError(_('Incorrect time slot'), code='invalid_time_slot')
    if not validate_table_seats(instance.table.num_of_seats, instance.num_of_customer_seats):
        raise ValidationError(_('Please choose a table with higher seats'), code='invalid_table_seats')
    if not validate_reservations_overlapping(instance.table.id, instance.start_time, instance.end_time, instance.date):
        raise ValidationError(_('There is an already reservation for that time'), code='invalid_reservation')
    return instance



