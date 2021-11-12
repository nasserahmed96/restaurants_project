from django.test import TestCase
from .models import User, Group
# Create your tests here.


class UserTestCase(TestCase):
    def get_user_data(self):
        return {'user': {'password': 'secret', 'name': 'Nasser'}, 'groups': 'Admin'}

    def test_create_user_without_employee_number(self):
        user = User.objects.create_user(**self.get_user_data()['user'])
        user.groups.set([Group.objects.create(name=self.get_user_data()['groups']),])
        user.save()

    def test_create_user_with_correct_employee_number(self):
        user = User.objects.create_user(employee_number=1234, **self.get_user_data()['user'])
        user.groups.set([Group.objects.create(name=self.get_user_data()['groups']), ])
        user.save()

    def test_create_user_with_wrong_employee_number(self):
        user = User.objects.create_user(employee_number=12345, **self.get_user_data()['user'])
        user.groups.set([Group.objects.create(name=self.get_user_data()['groups']), ])
        user.save()
