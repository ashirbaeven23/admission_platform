# Admission Platform
Автоматизированная информационная система учёта абитуриентов колледжа на Django.

## Технологии
- Python 3
- Django
- SQLite
- Tailwind CSS
- ReportLab
- openpyxl

## Установка
git clone https://github.com/ashirbaeven23/admission_platform.git
cd admission_platform

## Создание виртуального окружения:
python -m venv venv

## Активация:
Windows:
venv\Scripts\activate
Linux/macOS:
source venv/bin/activate

## Установка зависимостей:
pip install -r requirements.txt

## Миграции:
python manage.py migrate

## Загрузка тестовых данных:
python manage.py loaddata fixtures/test_data.json

## Создание суперпользователя:
python manage.py createsuperuser

## Запуск проекта:
python manage.py runserver
