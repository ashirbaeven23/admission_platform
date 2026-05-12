import uuid

from apps.admissions.models import (
    Enrollment
)


def generate_enrollment_number():
    return str(
        uuid.uuid4()
    )[:8].upper()


def enroll_application(
    application
):
    existing_enrollment = (
        Enrollment.objects.filter(
            application=application
        ).first()
    )

    if existing_enrollment:
        return existing_enrollment

    application.status = (
        'enrolled'
    )

    application.save()

    enrollment = (
        Enrollment.objects.create(
            application=application,
            enrollment_number=generate_enrollment_number()
        )
    )

    return enrollment