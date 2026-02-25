# 🚀 CyberSec Django Portfolio Website

Welcome to the **CyberSec Django Portfolio Site**! This is a complete, production-ready full-stack portfolio web application built with a cybersecurity theme. It showcases projects, certifications, and provides a contact interface, along with an administrative dashboard.

---

## 🌟 Key Features

### 1. **Public Pages (Visitor Facing)**
- **Home**: A dynamic, terminal-themed landing page featuring simulated cryptography terminal interactions (MD5/SHA-512 hashing and decryption simulation).
- **About**: Information about the developer, skills, and background.
- **Projects**: A dynamic showcase of portfolio projects with images, descriptions, and links to GitHub/Live Demos.
- **Certificates**: Display of professional certifications (e.g., Certified Ethical Hacker).
- **Contact**: A secure contact form that saves messages directly to the database without relying on external email providers.

### 2. **Authentication & Administration**
- **User Authentication**: Secure Signup, Login, and Logout functionality.
- **Dashboard**: A restricted-access management dashboard to oversee projects and certificates.
- **Role-Based Access**: Dashboard access is restricted to administrators only. 

### 3. **RESTful API**
- Includes a fully functional API built with Django REST Framework (DRF) for external integrations.
- Endpoints available for retrieving/creating projects and submitting contact messages.

---

## 🛠️ Technology Stack

- **Backend Framework**: Django 6.0+
- **Database**: PostgreSQL
- **API**: Django REST Framework (DRF)
- **Frontend Requirements**: HTML5, Vanilla CSS (Custom dark/cybersecurity terminal aesthetics, glassmorphism), Vanilla JavaScript.
- **Environment Management**: `python-dotenv` for secure secret management.

---

## 📂 Project Architecture

The Django project is modularized into several dedicated "apps" for separation of concerns:

- `portfolio_site/`: The main configuration package (`settings.py`, `urls.py`).
- `accounts_app/`: Handles user authentication, profile creation, and the secure dashboard.
- `projects_app/`: Manages the core portfolio content including `Project` and `Certificate` models and views.
- `contact_app/`: Manages the contact form submissions and the `ContactMessage` model.
- `api_app/`: Exposes REST endpoints for the portfolio data.
- `templates/`: Global HTML templates using Django Template Language.
- `static/`: Custom CSS styling, JavaScript, and static image assets.
- `media/`: User-uploaded content (project images, certificate images).

---

## ⚙️ Setup & Installation Instructions

Follow these steps to get the project running on your local machine.

### Prerequisites
- **Python 3.8+** installed.
- **PostgreSQL** installed and running locally.

### 1. Clone & Navigate
Navigate to the project directory:
```bash
cd ~/Downloads/portfolio_site
```

### 2. Virtual Environment
Create and activate a virtual environment to isolate dependencies:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
Install all required Python packages:
```bash
pip install -r requirements.txt
```
*(If `requirements.txt` is missing, install the core dependencies manually: `pip install django psycopg2-binary djangorestframework pillow python-dotenv`)*

### 4. Environment Variables
Create a `.env` file in the root directory (alongside `manage.py`) for sensitive configuration:
```env
# Example .env file mapping
EMAIL_HOST_USER="your-email@gmail.com"
EMAIL_HOST_PASSWORD="your-app-password"
```

### 5. Database Configuration
Ensure your PostgreSQL server is active.
1. Access the PostgreSQL prompt: `psql postgres`
2. Create the database: `CREATE DATABASE portfolio_db;`
3. If necessary, adjust `DATABASES` in `portfolio_site/settings.py` for your local DB username/password.

### 6. Migrations
Apply the database models to your Postgres database:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create Superuser (Admin)
To access the Django Admin panel and the restricted Dashboard, create a superuser account:
```bash
python manage.py createsuperuser
```
*(Follow the prompts to set a username, email, and password).*

### 8. Run the Development Server
Start the local Django server:
```bash
python manage.py runserver
```
Visit http://127.0.0.1:8000 in your browser to view the application!

---

## 🔌 API Endpoints Documentation

The application exposes a REST API for viewing and adding data.

| Endpoint | HTTP Method | Description |
|----------|-------------|-------------|
| `/api/projects/` | GET | List all portfolio projects. |
| `/api/projects/` | POST | Create a new project (Requires Auth/Admin). |
| `/api/projects/<slug>/` | GET | Retrieve details of a specific project by its slug. |
| `/api/contact/` | POST | Submit a new contact message. |

---

## 🔒 Security Notes
- **No Third-Party Email Storage**: Contact messages are saved directly to the database to avoid reliance on unauthenticated SMTP relays.
- **Environment Variables**: Sensitive keys (like Email app passwords) are stored securely in `.env`.
- **Custom 404 Page**: A styled 404 error page restricts users from seeing default Django error traces during dead-end navigation.

---
*Developed as a premier demonstration of Full-Stack Django Engineering.*
