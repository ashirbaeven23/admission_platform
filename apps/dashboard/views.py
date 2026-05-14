from django.contrib.auth.mixins import (
    LoginRequiredMixin
)
from django.core.paginator import (
    Paginator
)
from apps.admissions.services.ranking_service import (
    calculate_rankings
)
from apps.admissions.services.excel_service import (
    export_enrollments_excel
)
from django.views.generic import (
    TemplateView
)
from django.db.models import Q

from apps.admissions.models import (
    ActivityLog,
    Notification,
)
from apps.accounts.mixins import (
    DashboardAccessMixin
)
from apps.admissions.services.enrollment_service import (
    enroll_application,
)

from django.db.models import Count

from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
)

from django.views import View

from apps.accounts.mixins import (
    ManagerRequiredMixin,
    StatisticsRequiredMixin,
    EnrollmentRequiredMixin,
    AdminRequiredMixin,
)

from apps.admissions.models import (
    ApplicantProfile,
    Application,
)

from apps.education.models import (
    Department,
    Speciality,
)


class DashboardIndexView(
    ManagerRequiredMixin,
    View
):
    template_name = 'dashboard/index.html'

    def get(self, request):
        total_applications = (
            Application.objects.count()
        )

        approved_applications = (
            Application.objects.filter(
                status='approved'
            ).count()
        )

        enrolled_applications = (
            Application.objects.filter(
                status='enrolled'
            ).count()
        )

        recent_applications = (
            Application.objects
            .select_related(
                'applicant',
                'speciality'
            )
            .order_by('-created_at')[:8]
        )

        top_specialities = (
            Speciality.objects
            .annotate(
                total_applications=Count(
                    'applications'
                )
            )
            .order_by(
                '-total_applications'
            )[:5]
        )
        activities = (
            ActivityLog.objects
            .select_related('user')[:10]
        )

        notifications = (
            Notification.objects
            .filter(
                user=request.user
            )[:10]
        )

        return render(
            request,
            self.template_name,
            {
                'total_applications': total_applications,

                'approved_applications': approved_applications,

                'enrolled_applications': enrolled_applications,

                'recent_applications': recent_applications,

                'top_specialities': top_specialities,

                'activities': activities,

                'notifications': notifications,
            }
        )


class ApplicationsView(
    ManagerRequiredMixin,
    View
):
    template_name = (
        'dashboard/applications.html'
    )

    def get(self, request):
        search = request.GET.get(
            'search',
            ''
        )

        status = request.GET.get(
            'status',
            ''
        )

        applications = (
            Application.objects
            .select_related(
                'applicant',
                'speciality'
            )
            .order_by('-created_at')
        )

        if search:
            applications = (
                applications.filter(
                    Q(
                        applicant__first_name__icontains=search
                    )
                    |
                    Q(
                        applicant__last_name__icontains=search
                    )
                    |
                    Q(
                        speciality__title__icontains=search
                    )
                )
            )

        if status:
            applications = (
                applications.filter(
                    status=status
                )
            )

        paginator = Paginator(
            applications,
            10
        )

        page_number = request.GET.get(
            'page'
        )

        page_obj = paginator.get_page(
            page_number
        )

        return render(
            request,
            self.template_name,
            {
                'page_obj': page_obj,
                'search': search,
                'status': status,
            }
        )


class ApplicationDetailView(
    ManagerRequiredMixin,
    View
):
    template_name = (
        'dashboard/application_detail.html'
    )

    def get(self, request, pk):
        application = get_object_or_404(
            Application.objects.select_related(
                'applicant',
                'speciality'
            ),
            pk=pk
        )

        return render(
            request,
            self.template_name,
            {
                'application': application
            }
        )


class UpdateApplicationStatusView(
    ManagerRequiredMixin,
    View
):

    def post(self, request, pk):

        application = get_object_or_404(
            Application,
            pk=pk
        )

        status = request.POST.get(
            'status'
        )

        ALLOWED_STATUSES = [
            choice[0]
            for choice in Application.STATUS_CHOICES
        ]

        if status not in ALLOWED_STATUSES:

            return redirect(
                'dashboard:application_detail',
                pk=application.pk
            )

        application.status = status

        application.save()

        return redirect(
            'dashboard:application_detail',
            pk=application.pk
        )


class ApplicantsView(
    ManagerRequiredMixin,
    View
):
    template_name = (
        'dashboard/applicants.html'
    )

    def get(self, request):
        applicants = (
            ApplicantProfile.objects
            .all()
            .order_by('-created_at')
        )

        return render(
            request,
            self.template_name,
            {
                'applicants': applicants
            }
        )


class StatisticsView(
    StatisticsRequiredMixin,
    View
):
    template_name = (
        'dashboard/statistics.html'
    )

    def get(self, request):
        departments = (
            Department.objects
            .annotate(
                total_specialities=Count(
                    'specialities'
                )
            )
        )

        return render(
            request,
            self.template_name,
            {
                'departments': departments
            }
        )

class EnrollmentView(
    EnrollmentRequiredMixin,
    View
):
    template_name = (
        'dashboard/ranking/enrollment.html'
    )

    def post(self, request, pk):
        application = get_object_or_404(
            Application,
            pk=pk
        )

        enrollment = (
            enroll_application(
                application
            )
        )

        return render(
            request,
            self.template_name,
            {
                'enrollment': enrollment
            }
        )
class KanbanBoardView(
    ManagerRequiredMixin,
    View
):
    template_name = (
        'dashboard/kanban.html'
    )

    def get(self, request):
        new_applications = (
            Application.objects.filter(
                status='new'
            )
        )

        review_applications = (
            Application.objects.filter(
                status='review'
            )
        )

        approved_applications = (
            Application.objects.filter(
                status='approved'
            )
        )

        enrolled_applications = (
            Application.objects.filter(
                status='enrolled'
            )
        )

        return render(
            request,
            self.template_name,
            {
                'new_applications': new_applications,
                'review_applications': review_applications,
                'approved_applications': approved_applications,
                'enrolled_applications': enrolled_applications,
            }
        )
class RankingView(
    DashboardAccessMixin,
    TemplateView
):

    template_name = (
        'dashboard/ranking.html'
    )

    def get_context_data(
        self,
        **kwargs
    ):

        calculate_rankings()

        context = super().get_context_data(
            **kwargs
        )

        context['applications'] = (
            Application.objects.select_related(
                'applicant',
                'speciality'
            ).order_by(
                'speciality',
                'ranking_position'
            )
        )

        return context
class ExportExcelView(
    ManagerRequiredMixin,
    View
):

    def get(
        self,
        request
    ):

        return export_enrollments_excel()
class EnrollmentOrderView(
    ManagerRequiredMixin,
    TemplateView
):

    template_name = (
        'dashboard/enrollment_order.html'
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