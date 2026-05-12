from django.views.generic import (
    DetailView,
    ListView,
)

from .models import (
    Event,
    FAQ,
    Gallery,
    News,
    Teacher,
)


class NewsListView(ListView):
    model = News

    template_name = (
        'content/news_list.html'
    )

    context_object_name = 'news'


class NewsDetailView(DetailView):
    model = News

    template_name = (
        'content/news_detail.html'
    )

    context_object_name = 'article'


class EventsListView(ListView):
    model = Event

    template_name = (
        'content/events.html'
    )

    context_object_name = 'events'


class TeachersListView(ListView):
    model = Teacher

    template_name = (
        'content/teachers.html'
    )

    context_object_name = 'teachers'


class GalleryListView(ListView):
    model = Gallery

    template_name = (
        'content/gallery.html'
    )

    context_object_name = 'gallery'


class FAQListView(ListView):
    model = FAQ

    template_name = (
        'content/faq.html'
    )

    context_object_name = 'faq'