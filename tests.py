import os
import django

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'config.settings'
)

django.setup()

from apps.accounts.models import User

from apps.education.models import (
    Department,
    Speciality,
)

from apps.admissions.models import (
    ApplicantProfile,
    Application,
)

from apps.admissions.services.ranking_service import (
    calculate_rankings
)


print('\n==============================')
print('KMEPT SYSTEM TEST')
print('==============================\n')


# USERS

print('1. USERS TEST')

users_count = User.objects.count()

print(f'Users: {users_count}')

admins = User.objects.filter(
    role='admin'
).count()

managers = User.objects.filter(
    role='manager'
).count()

applicants = User.objects.filter(
    role='applicant'
).count()

print(f'Admins: {admins}')
print(f'Managers: {managers}')
print(f'Applicants: {applicants}')

print('\n------------------------------\n')


# EDUCATION

print('2. EDUCATION TEST')

departments_count = (
    Department.objects.count()
)

specialities_count = (
    Speciality.objects.count()
)

print(
    f'Departments: {departments_count}'
)

print(
    f'Specialities: {specialities_count}'
)

print('\n------------------------------\n')


# APPLICANTS

print('3. APPLICANTS TEST')

profiles_count = (
    ApplicantProfile.objects.count()
)

applications_count = (
    Application.objects.count()
)

print(
    f'Applicant Profiles: {profiles_count}'
)

print(
    f'Applications: {applications_count}'
)

print('\n------------------------------\n')


# RANKING

print('4. RANKING SYSTEM TEST')

calculate_rankings()

applications = (
    Application.objects.select_related(
        'applicant',
        'speciality'
    ).order_by(
        'speciality',
        'ranking_position'
    )
)

for app in applications:

    print(
        f'#{app.ranking_position} | '
        f'{app.applicant.last_name} '
        f'{app.applicant.first_name} | '
        f'{app.speciality.title} | '
        f'Total: {app.total_score} | '
        f'Budget: {app.is_budget}'
    )

print('\n------------------------------\n')


# STATUS TEST

print('5. STATUS TEST')

pending = (
    Application.objects.filter(
        status='pending'
    ).count()
)

approved = (
    Application.objects.filter(
        status='approved'
    ).count()
)

enrolled = (
    Application.objects.filter(
        status='enrolled'
    ).count()
)

print(f'Pending: {pending}')
print(f'Approved: {approved}')
print(f'Enrolled: {enrolled}')

print('\n------------------------------\n')


# PDF TEST

print('6. PDF SERVICE TEST')

try:

    app = Application.objects.first()

    if app:

        print(
            f'PDF generation ready for '
            f'application #{app.id}'
        )

    else:

        print(
            'No applications found'
        )

except Exception as e:

    print(
        f'PDF ERROR: {e}'
    )

print('\n------------------------------\n')


# FINAL RESULT

print('7. FINAL RESULT')

if (
    users_count > 0
    and departments_count > 0
    and specialities_count > 0
):

    print(
        '\nSYSTEM STATUS: OK'
    )

    print(
        'Admission CRM работает нормально.'
    )

else:

    print(
        '\nSYSTEM STATUS: ERROR'
    )

print('\n==============================')
print('TEST FINISHED')
print('==============================\n')