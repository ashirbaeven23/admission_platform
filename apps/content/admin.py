from django.contrib import admin

from .models import (
    Event,
    FAQ,
    Gallery,
    News,
    Teacher,
)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }


admin.site.register(
    Teacher
)

admin.site.register(
    Gallery
)

admin.site.register(
    FAQ
)