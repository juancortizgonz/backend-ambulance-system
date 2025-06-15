# 🚑 Intelligent Ambulance Management System

## 📌 Project Overview

The **Intelligent Ambulance Management System** is a backend service built with **Django** and **Django Rest Framework (DRF)**. It provides a robust **RESTful API** to optimize emergency response times by efficiently managing ambulance dispatch, tracking, and hospital assignments.

### **🔹 Key Features:**
- **Real-time ambulance tracking**
- **Automated dispatch optimization**
- **Role-based access control (RBAC)**
- **REST API with token-based authentication**
- **OpenAPI 3.0 documentation (Swagger UI)**

---

## 📖 Table of Contents
1. [Requirements](#requirements)
2. [Installation & Setup](#installation--setup)
3. [Authentication](#authentication)
4. [Running the Application](#running-the-application)
5. [Testing](#testing)
6. [API Documentation](#api-documentation)
7. [Contributing](#contributing)

---

## 📌 Requirements
Ensure you have the following dependencies installed:

- **Python**: 3.12
- **pip**: 24.0
- **Django**: 5.1.2
- **Django Rest Framework**: 3.14.0
- **drf-spectacular** (for OpenAPI 3)
- **django-environ** (for environment variable management)
- **drf-spectacular**
- **flake8**
- **black**
- **psycopg2**
- **django-cors-headers**
- **requests**
- **pytest**
- **pytest-django**
- **requests**
- **celery**
- **django-celery-beat**

Install these dependencies via `pip` after setting up a virtual environment (see below).

---

## ⚙️ Installation & Setup

### **1️⃣ Clone the repository**
```bash
git clone git@github.com:juancortizgonz/backend-ambulance-system.git
cd backend-ambulance-system
```

### **2️⃣ Create and activate a virtual environment**
```bash
python -m venv venv
```
#### **Activate the virtual environment:**
- **Linux/Mac:**
  ```bash
  source venv/bin/activate
  ```
- **Windows:**
  ```bash
  .\venv\Scripts\activate
  ```

### **3️⃣ Install dependencies (local development)**
```bash
sudo apt update
sudo apt install redis
sudo service redis-server start
```
```bash
pip install -r requirements-dev.txt
```

### **4️⃣ Set up environment variables**
Create a `.env` file in the project root and configure it as follows:
```env
DEBUG=True

SECRET_KEY=secret

DB_ENGINE=django.db.backends.postgresql
DB_NAME=db_name
DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=postgres

DISTANCE_MATRIX_API=<your_api_key>

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=email
EMAIL_HOST_PASSWORD=password
```

### **5️⃣ Apply database migrations**
```bash
python manage.py migrate
```

### **6️⃣ Create a superuser (Admin Panel Access)**
```bash
python manage.py createsuperuser
```
Follow the prompts to set up an admin user.

### **7. Load the sample data**

To load the sample data uses the following command:

```bash
python manage.py loaddata api/fixtures/*.json
```

---

## 🔑 Authentication
This application uses **Token-Based Authentication**.

### **Obtain an Authentication Token**
Make a `POST` request to obtain an authentication token:
```bash
curl -X POST http://127.0.0.1:8000/api/v1/auth/ \
     -H "Content-Type: application/json" \
     -d '{"username": "admin", "password": "yourpassword"}'
```
### **Use the Token in Requests**
Add the token to the `Authorization` header:
```http
Authorization: Token <your-token>
```

### **Create Groups & Permissions**
Run the following command to automatically create predefined roles:
```bash
python manage.py create_groups
```

Ensure you add each new user to the corresponding role using the admin panel.

---

## 🚀 Running the Application

Start the development server:
```bash
python manage.py runserver
```
The application will be available at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

Start celery and redis server:
```bash
redis-server
celery -A backend-ambulance worker --loglevel=info
celery -A backend-ambulance beat --loglevel=info
```

---

## 🧪 Testing
Ensure you have installed the **development dependencies** (`requirements-dev.txt`). Then, run the tests using:
```bash
pytest api/tests/test_<filename>.py
```
Replace `<filename>` with the name of the test file.

---

## 📜 API Documentation
Access the **Swagger UI** for a full list of endpoints:
```plaintext
http://127.0.0.1:8000/api/v1/schema/swagger-ui/
```
Example API Request:
```bash
curl -X GET http://127.0.0.1:8000/api/v1/ambulances/ \
     -H "Authorization: Token <your-token>"
```

---

## 🤝 Contributing
To make a contribution, please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**:
   ```bash
   git checkout -b feature-branch
   ```
3. **Follow code style guidelines** (use `black` for formatting)
4. **Commit your changes**:
   ```bash
   git commit -m "Add new feature"
   ```
5. **Push the branch**:
   ```bash
   git push origin feature-branch
   ```
6. **Create a Pull Request**

### **Code Style Guidelines**
- Use **PEP8** for Python code style.
- Use `black` for formatting:
  ```bash
  black .
  ```
- Ensure tests pass before submitting a PR:
  ```bash
  pytest
  ```

---

## 📄 License
The license is not defined yet.

---

🚑 **Empowering emergency response through intelligent technology!** 🚀

