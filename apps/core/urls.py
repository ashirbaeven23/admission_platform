from django.urls import path
from .views import (
    PublicEnrollmentOrderView
)
from .views import HomeView

urlpatterns = [
    path(
        '',
        HomeView.as_view(),
        name='home'
    ),
    path(
    'orders/enrollment/',
    PublicEnrollmentOrderView.as_view(),
    name='public_enrollment_order'
),
]