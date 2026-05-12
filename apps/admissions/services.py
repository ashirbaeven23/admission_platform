from .models import Application


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
                '-applicant__gpa'
            )
        )

        ranking = 1

        for app in speciality_apps:

            gpa_score = int(
                app.applicant.gpa * 20
            )

            total = (
                app.exam_score +
                gpa_score
            )

            app.total_score = total

            app.ranking_position = ranking

            if ranking <= speciality.budget_places:

                app.is_budget = True
                app.is_recommended = True

            else:

                app.is_budget = False
                app.is_recommended = False

            app.save()

            ranking += 1