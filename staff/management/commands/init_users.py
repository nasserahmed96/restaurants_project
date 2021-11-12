from django.core.management import BaseCommand
from django.contrib.auth.models import Group, Permission
from staff.models import User

class Command(BaseCommand):
    def handle(self, *args, **options):
        groups = ['Admin', 'Employee']
        #Group.objects.bulk_create([Group(name=group_name) for group_name in groups])
        self.assign_permissions_to_groups()
        super_user = {'name': 'nasser', 'password': 'secret'}
        super_user = User.objects.create_superuser(**super_user)
        super_user.groups.set([Group.objects.get(name='Admin'),])

    def assign_permissions_to_groups(self):
        permissions = ['add_user', 'view_restauranttable', 'add_restauranttable']
        Group.objects.get(name="Admin").permissions.set(Permission.objects.filter(codename__in=permissions))
