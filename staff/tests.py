from django.test import TestCase
from .models import User, Group
# Create your tests here.

class UserTestCase(TestCase):

    def get_user_data(self):
        groups = ['Admin', 'Employee']
        Group.objects.bulk_create([Group(name=group_name) for group_name in groups])
        admin_role = Group.objects.get(name='Admin')
        return {'password': 'secret', 'name': 'Nasser', 'role': admin_role}

    def test_create_user_without_employee_number(self):
        User.objects.create_user(**self.get_user_data())

    def test_create_user_with_correct_employee_number(self):
        print("Testing user with 1234 employee number")
        user = self.get_user_data()
        user["employee_number"] = 12345
        User.objects.create_user(**user)

    def test_create_user_with_wrong_employee_number(self):
        print("Testing user with: 123a")
        user = self.get_user_data()
        user["employee_number"] = '123a'
        User.objects.create_user(**user)
