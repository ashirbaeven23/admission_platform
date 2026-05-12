from django.contrib.auth.mixins import (
    UserPassesTestMixin
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin
)
from django.shortcuts import redirect
class AdminRequiredMixin(
    UserPassesTestMixin
):
    def test_func(self):
        user = self.request.user

        return (
            user.is_authenticated
            and (
                user.role == 'admin'
                or user.is_superuser
            )
        )


class ManagerRequiredMixin(
    UserPassesTestMixin
):
    def test_func(self):
        user = self.request.user

        return (
            user.is_authenticated
            and (
                user.can_manage_applications
                or user.is_superuser
            )
        )


class StatisticsRequiredMixin(
    UserPassesTestMixin
):
    def test_func(self):
        user = self.request.user

        return (
            user.is_authenticated
            and (
                user.can_view_statistics
                or user.is_superuser
            )
        )


class EnrollmentRequiredMixin(
    UserPassesTestMixin
):
    def test_func(self):
        user = self.request.user

        return (
            user.is_authenticated
            and (
                user.can_enroll_students
                or user.is_superuser
            )
        )


class UserManagementRequiredMixin(
    UserPassesTestMixin
):
    def test_func(self):
        user = self.request.user

        return (
            user.is_authenticated
            and (
                user.can_manage_users
                or user.is_superuser
            )
        )
class DashboardAccessMixin(
    LoginRequiredMixin
):

    def dispatch(
        self,
        request,
        *args,
        **kwargs
    ):

        if request.user.role in [
            'admin',
            'manager'
        ]:

            return super().dispatch(
                request,
                *args,
                **kwargs
            )

        return redirect(
            'accounts:login'
        )