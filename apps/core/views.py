from django.views.generic import (
    TemplateView
)

from apps.education.models import (
    Department,
    Speciality,
)

from apps.admissions.models import (
    Application
)
from django.views.generic import (
    TemplateView
)

from apps.admissions.models import (
    Application
)


class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(
        self,
        **kwargs
    ):
        context = super().get_context_data(
            **kwargs
        )

        context['specialities'] = (
            Speciality.objects.filter(
                is_active=True
            )[:6]
        )

        context['departments'] = (
            Department.objects.all()[:4]
        )

        context['total_students'] = 2500

        context['total_specialities'] = (
            Speciality.objects.count()
        )

        context['total_applications'] = (
            Application.objects.count()
        )

        return context
class PublicEnrollmentOrderView(
    TemplateView
):

    template_name = (
        'public/enrollment_order.html'
    )

    def get_context_data(
        self,
        **kwargs
    ):

        context = super().get_context_data(
            **kwargs
        )

        context['applications'] = (
            Application.objects.select_related(
                'applicant',
                'speciality'
            ).filter(
                is_recommended=True
            ).order_by(
                'ranking_position'
            )
        )

        return context