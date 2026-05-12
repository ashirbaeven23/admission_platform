from django.contrib import admin

from .models import Department
from .models import Speciality


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }

    list_display = (
        'name',
        'created_at',
    )


@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }

    list_display = (
        'title',
        'department',
        'duration',
        'budget_places',
        'is_active',
    )

    list_filter = (
        'department',
        'is_active',
    )

    search_fields = (
        'title',
        'code',
    )