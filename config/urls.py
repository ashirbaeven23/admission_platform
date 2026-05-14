from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin

from django.urls import include
from django.urls import path


urlpatterns = [

    path(
        'admin/',
        admin.site.urls
    ),

    path(
        '',
        include('apps.core.urls')
    ),

    path(
        'accounts/',
        include('apps.accounts.urls')
    ),

    path(
        'education/',
        include('apps.education.urls')
    ),

    path(
        'admissions/',
        include('apps.admissions.urls')
    ),

    path(
        'dashboard/',
        include('apps.dashboard.urls')
    ),

    path(
        '',
        include('apps.content.urls')
    ),

]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)

urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
)