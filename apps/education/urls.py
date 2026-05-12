from django.urls import path

from .views import (
    SpecialityDetailView,
    SpecialityListView,
)

app_name = 'education'

urlpatterns = [
    path(
        'specialities/',
        SpecialityListView.as_view(),
        name='speciality_list'
    ),

    path(
        'specialities/<slug:slug>/',
        SpecialityDetailView.as_view(),
        name='speciality_detail'
    ),
]