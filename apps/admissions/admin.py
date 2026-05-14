from django.contrib import admin

from .models import (
    ApplicantProfile,
    Application,
)


@admin.register(ApplicantProfile)
class ApplicantProfileAdmin(
    admin.ModelAdmin
):
    list_display = (
        'last_name',
        'first_name',
        'phone',
        'graduation_year',
    )

    search_fields = (
        'last_name',
        'first_name',
        'iin',
    )


@admin.register(Application)
class ApplicationAdmin(
    admin.ModelAdmin
):

    list_display = (
        'applicant',
        'speciality',
        'status',
        'exam_score',
        'total_score',
        'ranking_position',
        'is_budget',
        'created_at',
    )

    list_filter = (
        'status',
        'speciality',
        'is_budget',
    )

    search_fields = (
        'applicant__first_name',
        'applicant__last_name',
    )