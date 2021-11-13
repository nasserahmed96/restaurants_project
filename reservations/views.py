import datetime
import json
from django.core.exceptions import ValidationError
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth.decorators import permission_required
from django.views.decorators.csrf import ensure_csrf_cookie
from .serializers import ReservationSerializer
from .models import Reservation, RestaurantTable


@api_view(['POST'])
@permission_required('reservations.add_reservation', raise_exception=True)
@ensure_csrf_cookie
def create_reservation(request):
    try:
        reservation_serializer = ReservationSerializer(data=request.data)
        if reservation_serializer.is_valid():
            reservation_serializer.save()
            return Response(reservation_serializer.data, status=status.HTTP_201_CREATED)
        return Response(reservation_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except ValidationError as e:
        return Response(e.message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_required('reservations.view_reservation', raise_exception=True)
@ensure_csrf_cookie
def get_time_slots(request):
    time_slots = []
    minimum_number_of_seats = RestaurantTable.objects.filter(num_of_seats__gte=request.GET['num_of_customer_seats']).order_by('num_of_seats').first().num_of_seats
    allowed_tables = RestaurantTable.objects.filter(num_of_seats=minimum_number_of_seats)
    today = datetime.datetime.now().date()
    for table in allowed_tables:
        reservations = Reservation.objects.filter(date=today,
                                                  start_time__gte=datetime.datetime.now().time(),
                                                  table=table)
        time_slots.append({'start_time': datetime.datetime.now().time(),
                           'end_time': reservations.first().start_time,
                           'table': table.id}) if any(reservations) else ""
        print("Reservations: ", reservations)
        try:
            for i in range(0, len(reservations) + 1):
                time_slot = dict()
                time_slot['start_time'] = reservations[i].end_time
                time_slot['end_time'] = reservations[i + 1].start_time
                time_slot['table'] = table.id
                time_slots.append(time_slot)
        except IndexError:
            pass
    paginator = PaginationWithPagesCount()
    paginator.page_size = 1
    paginator.paginate_queryset(time_slots, request)
    return paginator.get_paginated_response(time_slots)


class PaginationWithPagesCount(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'result': data
        })