from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('scout', 'Scout'),
        ('recruiter', 'Recruiter'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='scout')

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_groups",
        blank=True
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions",
        blank=True
    )
