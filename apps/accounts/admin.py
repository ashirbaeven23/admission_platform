from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    list_display = (
        'id',
        'username',
        'email',
        'role',
        'is_staff',
        'is_active',
    )

    list_filter = (
        'role',
        'is_staff',
        'is_active',
    )

    search_fields = (
        'username',
        'email',
    )

    ordering = (
        'id',
    )

    fieldsets = UserAdmin.fieldsets + (
        (
            'Roles and Permissions',
            {
                'fields': (
                    'role',
                    'can_manage_applications',
                    'can_manage_specialities',
                    'can_manage_users',
                    'can_view_statistics',
                    'can_enroll_students',
                )
            },
        ),
    )