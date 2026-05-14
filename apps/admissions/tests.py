from django.test import (
    TestCase,
    Client
)

from django.contrib.auth import (
    get_user_model
)

from apps.education.models import (
    Department,
    Speciality
)

from apps.admissions.models import (
    ApplicantProfile,
    Application
)

User = get_user_model()


class AdmissionSystemTests(
    TestCase
):
    def test_document_upload(self):

        from apps.admissions.models import ApplicantDocument

        document = ApplicantDocument.objects.create(
            applicant=self.profile,
            document_type='passport',
            file='documents/test.pdf'
        )

        self.assertEqual(
            document.document_type,
            'passport'
        )
    def test_ranking_calculation(self):

        application = Application.objects.create(
            applicant=self.profile,
            speciality=self.speciality,
            motivation_letter='Test motivation',
            exam_score=90,
            total_score=95,
            score=95
        )

        application.ranking_position = 1

        application.save()

        self.assertEqual(
            application.ranking_position,
            1
        )
    def test_enrollment(self):

        from apps.admissions.models import Enrollment

        application = Application.objects.create(
            applicant=self.profile,
            speciality=self.speciality,
            motivation_letter='Test motivation',
            status='approved',
            exam_score=90,
            total_score=95,
            score=95
        )

        enrollment = Enrollment.objects.create(
            application=application,
            enrollment_number='ENR-001'
        )

        self.assertEqual(
            enrollment.application.status,
            'approved'
        )

    def setUp(self):

        self.client = Client()

        self.user = User.objects.create_user(
            username='applicant',
            password='12345678',
            role='applicant'
        )

        self.manager = User.objects.create_user(
            username='manager',
            password='12345678',
            role='manager'
        )

        self.department = Department.objects.create(
            name='IT Department',
            description='Test department'
        )

        self.speciality = Speciality.objects.create(
            department=self.department,
            title='Cyber Security',
            code='09.02.07',
            short_description='Short description',
            full_description='Full description',
            duration='4 years',
            education_form='Full-time',
            tuition_fee=100000
        )

        self.profile = ApplicantProfile.objects.create(
            user=self.user,
            first_name='Erbol',
            last_name='Ashirbaev',
            middle_name='Serikovich',
            birth_date='2005-01-01',
            gender='male',
            citizenship='Kazakhstan',
            phone='+77001234567',
            address='Almaty',
            school_name='School 1',
            graduation_year=2023,
            gpa=4.5,
            passport_number='A1234567',
            iin='123456789012'
        )

    def test_user_creation(self):

        self.assertEqual(
            self.user.username,
            'applicant'
        )

    def test_application_creation(self):

        application = Application.objects.create(
            applicant=self.profile,
            speciality=self.speciality,
            exam_score=90
        )

        self.assertEqual(
            application.exam_score,
            90
        )

    def test_application_status(self):

        application = Application.objects.create(
            applicant=self.profile,
            speciality=self.speciality,
            status='new'
        )

        application.status = 'approved'

        application.save()

        self.assertEqual(
            application.status,
            'approved'
        )

    def test_application_access(self):

        application = Application.objects.create(
            applicant=self.profile,
            speciality=self.speciality
        )

        self.client.login(
            username='applicant',
            password='12345678'
        )

        response = self.client.get(
            f'/admissions/pdf/{application.id}/'
        )

        self.assertNotEqual(
            response.status_code,
            404
        )

    def test_speciality_creation(self):

        self.assertEqual(
            self.speciality.title,
            'Cyber Security'
        )

    def test_department_creation(self):

        self.assertEqual(
            self.department.name,
            'IT Department'
        )

    def test_profile_creation(self):

        self.assertEqual(
            self.profile.first_name,
            'Erbol'
        )