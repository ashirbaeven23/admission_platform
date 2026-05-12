from django.contrib.auth import login
from django.contrib.auth import logout

from django.shortcuts import redirect
from django.shortcuts import render

from django.views import View

from .forms import LoginForm
from .forms import RegisterForm


class LoginView(View):
    template_name = 'accounts/login.html'

    def get(self, request):
        form = LoginForm()

        return render(
            request,
            self.template_name,
            {
                'form': form
            }
        )

    def post(self, request):
        form = LoginForm(
            request,
            data=request.POST
        )

        if form.is_valid():
            user = form.get_user()

            login(
                request,
                user
            )

            if user.role == 'applicant':
                return redirect(
                    '/admissions/dashboard/'
                )

            return redirect(
                '/dashboard/'
            )

        return render(
            request,
            self.template_name,
            {
                'form': form
            }
        )


class RegisterView(View):
    template_name = 'accounts/register.html'

    def get(self, request):
        form = RegisterForm()

        return render(
            request,
            self.template_name,
            {
                'form': form
            }
        )

    def post(self, request):
        form = RegisterForm(
            request.POST
        )

        if form.is_valid():
            user = form.save()

            user.role = 'applicant'

            user.save()

            login(
                request,
                user
            )

            return redirect(
                '/admissions/dashboard/'
            )

        return render(
            request,
            self.template_name,
            {
                'form': form
            }
        )


class LogoutView(View):
    def get(self, request):
        logout(request)

        return redirect('/')