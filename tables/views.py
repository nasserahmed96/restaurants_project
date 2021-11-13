from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import permission_required
from django.views.decorators.csrf import ensure_csrf_cookie
from .serializers import TableSerializer, RestaurantTable


@api_view(['POST'])
@permission_required('tables.add_restauranttable', raise_exception=True)
@ensure_csrf_cookie
def create_table(request):
    table_serializer = TableSerializer(data=request.data, many=False)
    if table_serializer.is_valid():
        table_serializer.save()
        return Response(table_serializer.data, status=status.HTTP_201_CREATED)
    return Response(table_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_required('tables.add_restauranttable', raise_exception=True)
@ensure_csrf_cookie
def view_tables(request):
    tables_serializer = TableSerializer(RestaurantTable.objects.all(), many=True)
    return Response(tables_serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_required('tables.delete_restauranttable', raise_exception=True)
@ensure_csrf_cookie
def delete_table(request, table_id):
    RestaurantTable.objects.get(id=table_id).delete()
    return Response("Table has been deleted", status=status.HTTP_200_OK)
