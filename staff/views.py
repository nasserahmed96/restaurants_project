from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import permission_required
from django.views.decorators.csrf import ensure_csrf_cookie
from .serializers import CreateUserSerializer
# Create your views here.


@api_view(['POST'])
@permission_required('staff.add_user', raise_exception=True)
@ensure_csrf_cookie
def create_user(request):
    user_serialzier = CreateUserSerializer(data=request.data, many=False)
    if user_serialzier.is_valid():
        user_serialzier.save()
        return Response(user_serialzier.data, status=status.HTTP_201_CREATED)
    return Response(user_serialzier.errors, status=status.HTTP_400_BAD_REQUEST)
