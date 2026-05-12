from django.urls import path
from .views import (
    UploadDocumentsView,
    ApplicationPDFView,
)
from .views import (
    ApplicantDashboardView
)
from .views import (
    ApplyView,
    MyApplicationsView,
    SuccessView,
)

app_name = 'admissions'

urlpatterns = [
    path(
        'apply/',
        ApplyView.as_view(),
        name='apply'
    ),

    path(
        'success/',
        SuccessView.as_view(),
        name='success'
    ),

    path(
        'my-applications/',
        MyApplicationsView.as_view(),
        name='my_applications'
    ),
    path(
    'documents/',
    UploadDocumentsView.as_view(),
    name='documents'
    ),

    path(
    'pdf/<int:pk>/',
    ApplicationPDFView.as_view(),
    name='application_pdf'
    ),
    path(
    'dashboard/',
    ApplicantDashboardView.as_view(),
    name='dashboard'
    ),
]