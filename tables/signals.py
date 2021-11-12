import re
from django.db.models.signals import pre_save
from django.core.exceptions import ValidationError
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from .models import RestaurantTable


@receiver(pre_save, sender=RestaurantTable)
def validate_numb_of_seats(sender, instance, *args, **kwargs):
    if instance.num_of_seats not in range(1, 13):
        raise ValidationError(_('Number of seats must be between 1 and 12'), code='invalid_num_of_seats')
    return instance.num_of_seats
