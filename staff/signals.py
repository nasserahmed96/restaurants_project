import re
from django.db.models.signals import pre_save
from django.core.exceptions import ValidationError
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from .models import User


@receiver(pre_save, sender=User)
def validate_employee_number(sender, instance, *args, **kwargs):
    numbers_regex = re.compile(r'^[0-9]{4}$')
    if not numbers_regex.match(str(instance.employee_number)):
        raise ValidationError(_('employee_number must be exactly 4 number length'), code='invalid_employee_number')