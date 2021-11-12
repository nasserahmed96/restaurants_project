from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group
from .managers import CustomUserManager
# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    employee_number = models.CharField(max_length=4, null=False, blank=False, unique=True)
    name = models.CharField(max_length=45, null=False)
    groups = models.ManyToManyField(Group, related_name='user', verbose_name='groups')

    USERNAME_FIELD = 'employee_number'

    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = CustomUserManager()


    class Meta:
        db_table = "users"
        get_latest_by = 'employee_number'

    def __str__(self):
        return self.name

