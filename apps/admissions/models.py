from django.conf import settings

from django.db import models

from apps.education.models import (
    Speciality
)
from django.core.validators import (
    FileExtensionValidator
)

class ApplicantProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='applicant_profile'
    )

    first_name = models.CharField(
        max_length=255
    )

    last_name = models.CharField(
        max_length=255
    )

    middle_name = models.CharField(
        max_length=255,
        blank=True
    )

    birth_date = models.DateField()

    gender = models.CharField(
        max_length=50
    )

    citizenship = models.CharField(
        max_length=255
    )

    phone = models.CharField(
        max_length=50
    )

    address = models.TextField()

    school_name = models.CharField(
        max_length=255
    )

    graduation_year = models.PositiveIntegerField()

    gpa = models.DecimalField(
        max_digits=4,
        decimal_places=2
    )

    passport_number = models.CharField(
        max_length=100
    )

    iin = models.CharField(
        max_length=20
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class Application(models.Model):
    NEW = 'new'
    REVIEW = 'review'
    APPROVED = 'approved'
    REJECTED = 'rejected'
    ENROLLED = 'enrolled'

    STATUS_CHOICES = [
        (NEW, 'New'),
        (REVIEW, 'Review'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
        (ENROLLED, 'Enrolled'),
    ]

    applicant = models.ForeignKey(
        ApplicantProfile,
        on_delete=models.CASCADE,
        related_name='applications'
    )

    speciality = models.ForeignKey(
        Speciality,
        on_delete=models.CASCADE,
        related_name='applications'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=NEW
    )
    exam_score = models.PositiveIntegerField(
        default=0
    )

    total_score = models.PositiveIntegerField(
        default=0
    )

    ranking_position = models.PositiveIntegerField(
        default=0
    )

    is_budget = models.BooleanField(
        default=False
    )

    is_recommended = models.BooleanField(
        default=False
    )

    motivation_letter = models.TextField()

    score = models.PositiveIntegerField(
        default=0
    )

    comment = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.applicant} - {self.speciality}'
    
class Enrollment(models.Model):
    application = models.OneToOneField(
        Application,
        on_delete=models.CASCADE,
        related_name='enrollment'
    )

    enrollment_number = models.CharField(
        max_length=100,
        unique=True
    )

    enrolled_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.enrollment_number
    
class ApplicantDocument(models.Model):
    PASSPORT = 'passport'
    CERTIFICATE = 'certificate'
    PHOTO = 'photo'

    DOCUMENT_TYPES = [
        (PASSPORT, 'Passport'),
        (CERTIFICATE, 'Certificate'),
        (PHOTO, 'Photo'),
    ]

    applicant = models.ForeignKey(
        ApplicantProfile,
        on_delete=models.CASCADE,
        related_name='documents'
    )

    document_type = models.CharField(
        max_length=50,
        choices=DOCUMENT_TYPES
    )

    file = models.FileField(
    upload_to='documents/',
    validators=[
        FileExtensionValidator(
            allowed_extensions=[
                'pdf',
                'jpg',
                'jpeg',
                'png'
            ]
        )
    ]
)

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    verified = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.document_type
    
class ActivityLog(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    action = models.CharField(
        max_length=255
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.action


class Notification(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='notifications'
    )

    title = models.CharField(
        max_length=255
    )

    message = models.TextField()

    is_read = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title