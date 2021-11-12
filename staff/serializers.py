import re
from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group
from .models import User

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']


class CreateUserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        print("Password: ", validated_data.get("password"))
        return User.objects.create_user(employee_number=validated_data.get('employee_number', None),
                                        password=validated_data.pop("password"),
                                        **validated_data)

    def validate_password(self, password_plain_text):
        password_regex = re.compile(r'^[a-zA-Z0-9_\-\@\#\^\&\=\%\$\!\(\)\*\\\/]{6,}$')
        if not password_regex.match(password_plain_text):
            raise ValidationError(_("Password must be at least 6 characters long"), code='invalid_password')
        return password_plain_text

    def to_representation(self, instance):
        response = dict()
        response['name'] = instance.name
        response['employee_number'] = instance.employee_number
        response['role'] = GroupSerializer(instance.role, many=False).data
        return response

    class Meta:
        model = User
        fields = ['name', 'role', 'password']


