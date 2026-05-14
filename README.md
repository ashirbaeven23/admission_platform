# Admission Platform

АИС учёта абитуриентов колледжа на Django.

## Функциональность

- регистрация пользователей;
- подача заявлений;
- загрузка документов;
- управление специальностями;
- рейтинг абитуриентов;
- система зачисления;
- PDF генерация заявлений;
- административная панель.

## Технологии

- Python 3
- Django 5
- SQLite
- HTML/CSS
- Bootstrap/Tailwind
- ReportLab

## Установка проекта

```bash
git clone https://github.com/ashirbaeven23/admission_platform.git
```

## Создание виртуального окружения

```bash
python -m venv venv
```

## Активация окружения

Windows:

```bash
venv\Scripts\activate
```

## Установка зависимостей

```bash
pip install -r requirements.txt
```

## Миграции базы данных

```bash
python manage.py migrate
```

## Создание суперпользователя

```bash
python manage.py createsuperuser
```

## Загрузка тестовых данных

```bash
python manage.py loaddata fixtures/test_data.json
```

## Запуск проекта

```bash
python manage.py runserver
```

## Запуск тестов

```bash
python manage.py test apps.admissions.tests
```