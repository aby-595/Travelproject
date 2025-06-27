# ✈️ Travel Website (Django)

A Django-based web application designed to simulate a travel and tourism website. This project includes user interaction through login/registration and serves as a basic platform for displaying travel-related content.

---

## 🔧 Features

- User registration and login system
- Static home page with travel content
- Admin panel for backend management
- Django MVC structure using templates, views, and routing

---

## 🚀 Technologies Used

- Python 3.x
- Django
- HTML, CSS (Bootstrap if included)
- SQLite (Django default DB)

---

## 📁 Folder Overview

- `travelproject/` – Main Django project folder (`settings.py`, `urls.py`, `wsgi.py`, etc.)
- `travel/` – App directory for business logic (if exists; not fully visible in your repo)
- `templates/` – HTML files for frontend pages
- `static/` – CSS/JS files (if any)

---

## ▶️ How to Run This Project

> Make sure Python and Django are installed.

```bash
# 1. Clone the repo
git clone https://github.com/aby-595/Travelproject.git
cd Travelproject

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install Django
pip install django

# 4. Migrate and run
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
