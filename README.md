# Django Portfolio Site

A complete full-stack portfolio website built with Django, PostgreSQL, and plain CSS.

## Features
- **Public Pages**: Home, About, Projects, Contact.
- **Authentication**: Signup, Login, Logout, Dashboard.
- **Backend**: Django + PostgreSQL.
- **API**: Django REST Framework endpoints for Projects and Contact.
- **Styling**: Custom CSS (No frameworks).

## Prerequisites
- Python 3.8+
- PostgreSQL

## Setup Instructions

1.  **Navigate to Project Directory**:
    ```bash
    cd ~/Downloads/portfolio_site
    ```

2.  **Activate Virtual Environment**:
    ```bash
    source venv/bin/activate
    ```

3.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: If requirements.txt is missing, install manually: `pip install django psycopg2-binary djangorestframework pillow`)*

4.  **Database Configuration**:
    - Ensure PostgreSQL is running.
    - Create database: `createdb portfolio_db`
    - Update `portfolio_site/settings.py` if your DB user/password differs from default custom.

5.  **Run Migrations**:
    ```bash
    python manage.py migrate
    ```

6.  **Create Superuser** (Optional, for Admin access):
    ```bash
    python manage.py createsuperuser
    ```

7.  **Run Server**:
    ```bash
    python manage.py runserver
    ```

## API Endpoints
- Projects: `/api/projects/` (GET, POST-admin)
- Contact: `/api/contact/` (POST)

## Project Structure
- `accounts_app`: User profiles and auth.
- `projects_app`: Project management and public views.
- `contact_app`: Contact form logic.
- `api_app`: REST API configuration.
# portfolio
