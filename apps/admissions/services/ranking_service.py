from apps.admissions.models import (
    Application
)


def calculate_rankings():

    applications = (
        Application.objects.select_related(
            'applicant',
            'speciality'
        )
    )

    specialities = set()

    for app in applications:

        specialities.add(
            app.speciality
        )

    for speciality in specialities:

        speciality_apps = (
            Application.objects.filter(
                speciality=speciality
            ).order_by(
                '-exam_score',
                '-applicant__gpa',
                'created_at'
            )
        )

        ranking = 1

        for app in speciality_apps:

            gpa = float(
                app.applicant.gpa
            )

            if gpa < 0:
                gpa = 0

            if gpa > 5:
                gpa = 5

            # GPA переводится в 100-балльную систему
            gpa_score = int(
                gpa * 20
            )

            total = (
                app.exam_score +
                gpa_score
            )

            app.total_score = total

            app.ranking_position = ranking

            MIN_BUDGET_SCORE = 150

            if (
                ranking <= speciality.budget_places
                and total >= MIN_BUDGET_SCORE
            ):

                app.is_budget = True
                app.is_recommended = True

            else:

                app.is_budget = False
                app.is_recommended = True

            app.save()

            ranking += 1