from django.core.mail import (
    send_mail
)

from django.conf import settings


def send_application_notification(
    application
):
    send_mail(
        subject='Application Submitted',

        message=(
            f'Your application for '
            f'{application.speciality.title} '
            f'has been submitted.'
        ),

        from_email=(
            settings.DEFAULT_FROM_EMAIL
        ),

        recipient_list=[
            application.applicant.user.email
        ],

        fail_silently=True,
    )