# apps/admissions/views.py

from django.contrib.auth.mixins import (
    LoginRequiredMixin
)

from .forms import (
    ApplicantDocumentForm
)

from .services.activity_service import (
    create_activity,
    create_notification,
)
from .models import (
    ApplicantDocument,
    Notification,
)

from .services.pdf_service import (
    generate_application_pdf
)

from .services.notification_service import (
    send_application_notification
)
from django.views import View

from .forms import (
    ApplicantProfileForm,
    ApplicationForm,
)

from .models import (
    ApplicantProfile,
    Application,
)
from django.shortcuts import (
    redirect,
    render,
    get_object_or_404,
)


class ApplyView(
    LoginRequiredMixin,
    View
):

    template_name = (
        'admissions/apply.html'
    )

    def get(
        self,
        request
    ):

        profile_form = (
            ApplicantProfileForm()
        )

        application_form = (
            ApplicationForm()
        )

        return render(
            request,
            self.template_name,
            {
                'profile_form': profile_form,
                'application_form': application_form,
            }
        )

    def post(
        self,
        request
    ):

        profile_form = (
            ApplicantProfileForm(
                request.POST
            )
        )

        application_form = (
            ApplicationForm(
                request.POST
            )
        )

        if (
            profile_form.is_valid()
            and application_form.is_valid()
        ):

            applicant_profile, created = (
                ApplicantProfile.objects.get_or_create(
                    user=request.user,
                    defaults=profile_form.cleaned_data
                )
            )

            application = (
                application_form.save(
                    commit=False
                )
            )

            application.applicant = (
                applicant_profile
            )

            application.save()

            create_activity(
                request.user,
                'Подал новое заявление'
            )

            create_notification(
                request.user,
                'Заявление отправлено',
                'Ваше заявление успешно создано'
            )

            send_application_notification(
                application
            )

            return redirect(
                'admissions:success'
            )

        return render(
            request,
            self.template_name,
            {
                'profile_form': profile_form,
                'application_form': application_form,
            }
        )


class SuccessView(
    LoginRequiredMixin,
    View
):

    template_name = (
        'admissions/success.html'
    )

    def get(
        self,
        request
    ):

        return render(
            request,
            self.template_name
        )


class MyApplicationsView(
    LoginRequiredMixin,
    View
):

    template_name = (
        'admissions/my_applications.html'
    )

    def get(
        self,
        request
    ):

        applications = (
            Application.objects
            .select_related(
                'speciality',
                'applicant'
            )
            .filter(
                applicant__user=request.user
            )
        )

        return render(
            request,
            self.template_name,
            {
                'applications': applications
            }
        )


class UploadDocumentsView(
    LoginRequiredMixin,
    View
):

    template_name = (
        'dashboard/documents/documents.html'
    )

    def get(
        self,
        request
    ):

        form = (
            ApplicantDocumentForm()
        )

        documents = (
            ApplicantDocument.objects
            .filter(
                applicant__user=request.user
            )
        )

        return render(
            request,
            self.template_name,
            {
                'form': form,
                'documents': documents,
            }
        )

    def post(
        self,
        request
    ):

        form = ApplicantDocumentForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            applicant = (
                request.user
                .applicant_profile
            )

            document = form.save(
                commit=False
            )

            document.applicant = (
                applicant
            )

            document.save()

            return redirect(
                'admissions:documents'
            )

        documents = (
            ApplicantDocument.objects
            .filter(
                applicant__user=request.user
            )
        )

        return render(
            request,
            self.template_name,
            {
                'form': form,
                'documents': documents,
            }
        )


class ApplicationPDFView(
    LoginRequiredMixin,
    View
):

    def get(self, request, pk):

        if request.user.role == 'applicant':

            application = get_object_or_404(
                Application,
                pk=pk,
                applicant__user=request.user
            )

        else:

            application = get_object_or_404(
                Application,
                pk=pk
            )

        return generate_application_pdf(
            application
        )


class ApplicantDashboardView(
    LoginRequiredMixin,
    View
):

    template_name = (
        'admissions/dashboard.html'
    )

    def get(
        self,
        request
    ):

        applicant = (
            ApplicantProfile.objects
            .filter(
                user=request.user
            )
            .first()
        )

        applications = (
            Application.objects
            .select_related(
                'speciality'
            )
            .filter(
                applicant__user=request.user
            )
        )

        documents = (
            ApplicantDocument.objects
            .filter(
                applicant__user=request.user
            )
        )

        notifications = (
            Notification.objects
            .filter(
                user=request.user
            )[:10]
        )

        total_applications = (
            applications.count()
        )

        approved_count = (
            applications.filter(
                status='approved'
            ).count()
        )

        enrolled_count = (
            applications.filter(
                status='enrolled'
            ).count()
        )

        return render(
            request,
            self.template_name,
            {
                'applicant': applicant,

                'applications': applications,

                'documents': documents,

                'notifications': notifications,

                'total_applications': total_applications,

                'approved_count': approved_count,

                'enrolled_count': enrolled_count,
            }
        )