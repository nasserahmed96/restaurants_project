from rest_framework import serializers
from .models import RestaurantTable
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class TableSerializer(serializers.ModelSerializer):

    def validate_num_of_seats(self, num_of_seats):
        if num_of_seats not in range(1, 13):
            raise ValidationError(_('Number of seats must be between 1 and 12'), code='invalid_num_of_seats')
        return num_of_seats

    class Meta:
        model = RestaurantTable
        fields = ['number', 'num_of_seats']