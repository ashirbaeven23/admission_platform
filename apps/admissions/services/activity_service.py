from apps.admissions.models import (
    ActivityLog,
    Notification,
)


def create_activity(
    user,
    action
):
    ActivityLog.objects.create(
        user=user,
        action=action
    )


def create_notification(
    user,
    title,
    message
):
    Notification.objects.create(
        user=user,
        title=title,
        message=message
    )