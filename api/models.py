from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

restaurant_type_choices = (
    ("VEG", "VEG"),
    ("NON-VEG", "NON-VEG"),
)

roles = (
    ("superuser", "superuser"),
    ("admin", "admin"),
    ("guest", "guest")
)
# Create your models here.


class Resto(models.Model):
    restaurant_id = models.IntegerField(primary_key=True)
    restaurant_name = models.CharField(max_length=20)
    restaurant_type = models.CharField(
        max_length=20, blank=True, null=True, choices=restaurant_type_choices)
    restaurant_add = models.TextField()
    restaurant_website = models.CharField(max_length=255)

    def __str__(self):
        return self.restaurant_name


class userAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    role = models.CharField(max_length=20, blank=False,
                            null=False, default='guest', choices=roles)

    objects = userAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone']

    def getName(self):
        return self.name

    def getShortName(self):
        return self.name

    def __str__(self):
        return self.name
