from django.db import models

from django.utils.text import slugify


class Department(models.Model):
    name = models.CharField(
        max_length=255
    )

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    description = models.TextField()

    image = models.ImageField(
        upload_to='departments/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['name']

    def save(self, *args, **kwargs):
        self.slug = slugify(
            self.name
        )

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Speciality(models.Model):
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='specialities'
    )

    title = models.CharField(
        max_length=255
    )

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    code = models.CharField(
        max_length=20
    )

    image = models.ImageField(
        upload_to='specialities/',
        blank=True,
        null=True
    )

    short_description = models.TextField()

    full_description = models.TextField()

    duration = models.CharField(
        max_length=100
    )

    education_form = models.CharField(
        max_length=100
    )

    budget_places = models.PositiveIntegerField(
        default=0
    )

    paid_places = models.PositiveIntegerField(
        default=0
    )

    tuition_fee = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    employment_rate = models.PositiveIntegerField(
        default=0
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['title']

    def save(self, *args, **kwargs):
        self.slug = slugify(
            self.title
        )

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title