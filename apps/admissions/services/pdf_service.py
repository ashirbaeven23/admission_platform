from io import BytesIO

from django.http import HttpResponse

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from reportlab.pdfbase import pdfmetrics

from reportlab.pdfbase.cidfonts import (
    UnicodeCIDFont
)

from apps.admissions.models import (
    Application
)


pdfmetrics.registerFont(
    UnicodeCIDFont(
        'HYSMyeongJo-Medium'
    )
)


def generate_application_pdf(
    application
):

    buffer = BytesIO()

    document = SimpleDocTemplate(
        buffer
    )

    styles = getSampleStyleSheet()

    style = styles['Normal']

    style.fontName = (
        'HYSMyeongJo-Medium'
    )

    title_style = styles['Heading1']

    title_style.fontName = (
        'HYSMyeongJo-Medium'
    )

    elements = []

    elements.append(

        Paragraph(
            'ЗАЯВЛЕНИЕ АБИТУРИЕНТА',
            title_style
        )

    )

    elements.append(
        Spacer(1, 20)
    )

    applicant = application.applicant

    elements.append(

        Paragraph(
            (
                f'ФИО: '
                f'{applicant.last_name} '
                f'{applicant.first_name}'
            ),
            style
        )

    )

    elements.append(
        Spacer(1, 10)
    )

    elements.append(

        Paragraph(
            (
                f'Специальность: '
                f'{application.speciality.title}'
            ),
            style
        )

    )

    elements.append(
        Spacer(1, 10)
    )

    elements.append(

        Paragraph(
            (
                f'GPA: '
                f'{applicant.gpa}'
            ),
            style
        )

    )

    elements.append(
        Spacer(1, 10)
    )

    elements.append(

        Paragraph(
            (
                f'Баллы экзамена: '
                f'{application.exam_score}'
            ),
            style
        )

    )

    elements.append(
        Spacer(1, 10)
    )

    elements.append(

        Paragraph(
            (
                f'Статус: '
                f'{application.status}'
            ),
            style
        )

    )

    elements.append(
        Spacer(1, 40)
    )

    elements.append(

        Paragraph(
            (
                'KMEPT — Колледж мировой '
                'экономики и передовых технологий'
            ),
            style
        )

    )

    document.build(
        elements
    )

    pdf = buffer.getvalue()

    buffer.close()

    response = HttpResponse(
        content_type='application/pdf'
    )

    response[
        'Content-Disposition'
    ] = (
        f'attachment; '
        f'filename=application_{application.id}.pdf'
    )

    response.write(pdf)

    return response