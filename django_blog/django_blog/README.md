# Django Blog Project

A simple Django blog with user authentication and profile management.

## Features

- List and view blog posts
- User registration, login, logout
- Profile page to view/update email
- Static files: CSS, JS, images

## Setup

1. **Activate virtual environment**

````bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

2. **Install dependencies**
```bash
pip install django

3. **Apply migrations**
```bash
python manage.py makemigrations
python manage.py migrate

4. **Create superuser** (optional)
```bash
python manage.py createsuperuser

5. **Run server**
```bash
python manage.py runserver
Visit http://127.0.0.1:8000/

URLs
/ → Blog index

/post/<id>/ → Post detail

/register/ → User registration

/login/ → User login

/logout/ → Logout

/profile/ → Profile management

````
