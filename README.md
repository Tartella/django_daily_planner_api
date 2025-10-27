# Django Backend API for Daily Planner

Backend API built with Django + Django REST Framework.

## Features
- Model: Task(title, description, due_date, is_completed, created_at)
- CRUD API endpoints
- RESTful routes with Django REST Framework
- CORS enabled for React frontend

## Run locally
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
