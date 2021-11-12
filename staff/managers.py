from django.contrib.auth.models import UserManager
from django.contrib.auth.models import Group

class CustomUserManager(UserManager):
    def create_user(self, password, employee_number=None, **extra_fields):
        print("Employee number: ", employee_number)
        new_employee_number = self.create_employee_number() if not employee_number else employee_number
        print("New employee number: ", new_employee_number)
        user = self.model(employee_number=new_employee_number, **extra_fields)
        print("Password: ", password)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, password, employee_number=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(password=password, employee_number=employee_number, **extra_fields)

    def create_employee_number(self):
        latest_user = int(self.model.objects.latest('employee_number').employee_number) if self.model.objects.filter().exists() else 0
        return str(latest_user+1).zfill(4)


