from django.contrib.auth.models import (
    AbstractUser
)

from django.db import models


class User(AbstractUser):
    ADMIN = 'admin'
    MANAGER = 'manager'
    APPLICANT = 'applicant'

    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (MANAGER, 'Manager'),
        (APPLICANT, 'Applicant'),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=APPLICANT
    )

    can_manage_applications = (
        models.BooleanField(
            default=False
        )
    )

    can_manage_specialities = (
        models.BooleanField(
            default=False
        )
    )

    can_manage_users = (
        models.BooleanField(
            default=False
        )
    )

    can_view_statistics = (
        models.BooleanField(
            default=False
        )
    )

    can_enroll_students = (
        models.BooleanField(
            default=False
        )
    )

    def save(self, *args, **kwargs):
        if self.role == self.ADMIN:
            self.can_manage_applications = True
            self.can_manage_specialities = True
            self.can_manage_users = True
            self.can_view_statistics = True
            self.can_enroll_students = True

        elif self.role == self.MANAGER:
            self.can_manage_applications = True
            self.can_view_statistics = True
            self.can_enroll_students = True

        super().save(*args, **kwargs)

    def __str__(self):
        return self.username