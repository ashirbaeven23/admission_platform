from django.views.generic import (
    DetailView,
    ListView,
)

from .models import Speciality


class SpecialityListView(ListView):
    model = Speciality

    template_name = (
        'education/speciality_list.html'
    )

    context_object_name = 'specialities'

    def get_queryset(self):
        return (
            Speciality.objects
            .select_related('department')
            .filter(is_active=True)
        )


class SpecialityDetailView(DetailView):
    model = Speciality

    template_name = (
        'education/speciality_detail.html'
    )

    context_object_name = 'speciality'