import uuid

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("Email should be provided"))
        email = self.normalize_email(email)

        new_user = self.model(email=email, **extra_fields)

        new_user.set_password(password)
        new_user.id = uuid.uuid4()
        print(new_user)
        new_user.save()

        return new_user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser should have is_staff as True"))

        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser should have is_superuser as True"))

        if extra_fields.get("is_active") is not True:
            raise ValueError(_("Superuser should have is_active as True"))

        return self.crate_user(email, password, **extra_fields)


class User(AbstractUser):
    # id = models.UUIDField(primary_key=True, editable=False)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=100, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return f"<User {self.email}"
