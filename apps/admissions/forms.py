from django import forms
import os
from .models import (
    ApplicantDocument,
    ApplicantProfile,
    Application,
)


INPUT_CLASS = (
    'w-full bg-slate-100 border border-slate-200 '
    'rounded-2xl px-6 py-5 outline-none '
    'focus:ring-4 focus:ring-blue-100 '
    'focus:border-blue-500 transition'
)


class ApplicantProfileForm(
    forms.ModelForm
):
    class Meta:
        model = ApplicantProfile

        fields = [
            'first_name',
            'last_name',
            'middle_name',
            'birth_date',
            'gender',
            'citizenship',
            'phone',
            'address',
            'school_name',
            'graduation_year',
            'gpa',
            'passport_number',
            'iin',
        ]

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Имя',
                    'class': INPUT_CLASS,
                }
            ),

            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Фамилия',
                    'class': INPUT_CLASS,
                }
            ),

            'middle_name': forms.TextInput(
                attrs={
                    'placeholder': 'Отчество',
                    'class': INPUT_CLASS,
                }
            ),

            'birth_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': INPUT_CLASS,
                }
            ),

            'gender': forms.Select(
                choices=[
                    ('male', 'Мужской'),
                    ('female', 'Женский'),
                ],
                attrs={
                    'class': INPUT_CLASS,
                }
            ),

            'citizenship': forms.TextInput(
                attrs={
                    'placeholder': 'Гражданство',
                    'class': INPUT_CLASS,
                }
            ),

            'phone': forms.TextInput(
                attrs={
                    'placeholder': '+7 777 777 77 77',
                    'class': INPUT_CLASS,
                }
            ),

            'address': forms.Textarea(
                attrs={
                    'placeholder': 'Адрес проживания',
                    'rows': 4,
                    'class': INPUT_CLASS,
                }
            ),

            'school_name': forms.TextInput(
                attrs={
                    'placeholder': 'Название школы',
                    'class': INPUT_CLASS,
                }
            ),

            'graduation_year': forms.NumberInput(
                attrs={
                    'placeholder': 'Год окончания',
                    'class': INPUT_CLASS,
                }
            ),

            'gpa': forms.NumberInput(
                attrs={
                    'placeholder': 'GPA / Средний балл',
                    'step': '0.01',
                    'class': INPUT_CLASS,
                }
            ),

            'passport_number': forms.TextInput(
                attrs={
                    'placeholder': 'Номер паспорта',
                    'class': INPUT_CLASS,
                }
            ),

            'iin': forms.TextInput(
                attrs={
                    'placeholder': 'ИИН',
                    'class': INPUT_CLASS,
                }
            ),
        }


class ApplicationForm(
    forms.ModelForm
):
    class Meta:
        model = Application

        fields = [
            'speciality',
            'motivation_letter',
        ]

        widgets = {
            'speciality': forms.Select(
                attrs={
                    'class': INPUT_CLASS,
                }
            ),

            'motivation_letter': forms.Textarea(
                attrs={
                    'placeholder': (
                        'Расскажите почему хотите '
                        'поступить на эту специальность'
                    ),

                    'rows': 7,

                    'class': INPUT_CLASS,
                }
            ),
        }


class ApplicantDocumentForm(
    forms.ModelForm
):

    class Meta:
        model = ApplicantDocument

        fields = [
            'document_type',
            'file',
        ]

        widgets = {
            'document_type': forms.Select(
                attrs={
                    'class': INPUT_CLASS,
                }
            ),

            'file': forms.ClearableFileInput(
                attrs={
                    'class': (
                        'w-full border-2 border-dashed '
                        'border-slate-300 rounded-2xl '
                        'p-8 bg-slate-50'
                    )
                }
            ),
        }

    def clean_file(self):

        file = self.cleaned_data.get(
            'file'
        )

        if file:

            max_size = 5 * 1024 * 1024

            if file.size > max_size:

                raise forms.ValidationError(
                    'Размер файла не должен превышать 5 MB'
                )

            allowed_types = [
                'application/pdf',
                'image/jpeg',
                'image/png',
            ]

            if file.content_type not in allowed_types:

                raise forms.ValidationError(
                    'Допустимы только PDF, JPG и PNG файлы'
                )

            allowed_extensions = [
                '.pdf',
                '.jpg',
                '.jpeg',
                '.png',
            ]

            ext = os.path.splitext(
                file.name
            )[1].lower()

            if ext not in allowed_extensions:

                raise forms.ValidationError(
                    'Недопустимый формат файла'
                )

        return file