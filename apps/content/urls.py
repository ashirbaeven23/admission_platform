from django.urls import path

from .views import (
    EventsListView,
    FAQListView,
    GalleryListView,
    NewsDetailView,
    NewsListView,
    TeachersListView,
)

urlpatterns = [
    path(
        'news/',
        NewsListView.as_view(),
        name='news'
    ),

    path(
        'news/<slug:slug>/',
        NewsDetailView.as_view(),
        name='news_detail'
    ),

    path(
        'events/',
        EventsListView.as_view(),
        name='events'
    ),

    path(
        'teachers/',
        TeachersListView.as_view(),
        name='teachers'
    ),

    path(
        'gallery/',
        GalleryListView.as_view(),
        name='gallery'
    ),

    path(
        'faq/',
        FAQListView.as_view(),
        name='faq'
    ),
]