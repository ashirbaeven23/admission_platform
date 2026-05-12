from django.db import models

from django.utils.text import slugify


class News(models.Model):
    title = models.CharField(
        max_length=255
    )

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    image = models.ImageField(
        upload_to='news/',
        blank=True,
        null=True
    )

    short_description = (
        models.TextField()
    )

    content = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    is_published = models.BooleanField(
        default=True
    )

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(
                self.title
            )

        super().save(
            *args,
            **kwargs
        )

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(
        max_length=255
    )

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    image = models.ImageField(
        upload_to='events/',
        blank=True,
        null=True
    )

    description = models.TextField()

    location = models.CharField(
        max_length=255
    )

    event_date = models.DateTimeField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(
                self.title
            )

        super().save(
            *args,
            **kwargs
        )

    def __str__(self):
        return self.title


class Teacher(models.Model):
    full_name = models.CharField(
        max_length=255
    )

    position = models.CharField(
        max_length=255
    )

    photo = models.ImageField(
        upload_to='teachers/',
        blank=True,
        null=True
    )

    bio = models.TextField()

    experience = models.PositiveIntegerField(
        default=1
    )

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.full_name


class Gallery(models.Model):
    title = models.CharField(
        max_length=255
    )

    image = models.ImageField(
        upload_to='gallery/'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


class FAQ(models.Model):
    question = models.CharField(
        max_length=255
    )

    answer = models.TextField()

    order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.question