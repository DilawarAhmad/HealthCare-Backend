# Healthcare Backend API

A RESTful Healthcare Backend built using Django, Django REST Framework (DRF), PostgreSQL, and JWT Authentication.

## Features

- User Registration
- User Login with JWT Authentication
- Doctor Management APIs
- Patient Management APIs
- Patient-Doctor Mapping APIs
- PostgreSQL Database
- Environment Variable Configuration
- Error Handling & Validation

---

## Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- JWT Authentication (SimpleJWT)
- Postman
- Git & GitHub

---

## Installation

### Clone Repository

```bash
git clone https://github.com/DilawarAhmad/HealthCare-Backend.git
cd healthcare-backend
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Mac/Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
DB_NAME=healthcare_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

---

## Database Setup

Create PostgreSQL database:

```sql
CREATE DATABASE healthcare_db;
```

Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Run Server

```bash
python manage.py runserver
```

Server:

```text
http://127.0.0.1:8000/
```

---

# Authentication APIs

## Register User

POST

```text
/api/auth/register/
```

Request

```json
{
  "first_name": "Adil",
  "last_name": "Wagay",
  "email": "adil@gmail.com",
  "password": "adil12345"
}
```

---

## Login User

POST

```text
/api/auth/login/
```

Request

```json
{
  "email": "adil@gmail.com",
  "password": "adil12345"
}
```

Response

```json
{
  "refresh": "...",
  "access": "..."
}
```

---

# Doctor APIs

| Method | Endpoint | Description |
|----------|----------|----------|
| POST | /api/doctors/ | Create Doctor |
| GET | /api/doctors/ | Get All Doctors |
| GET | /api/doctors/{id}/ | Get Doctor |
| PUT | /api/doctors/{id}/ | Update Doctor |
| DELETE | /api/doctors/{id}/ | Delete Doctor |

---

# Patient APIs

| Method | Endpoint | Description |
|----------|----------|----------|
| POST | /api/patients/ | Create Patient |
| GET | /api/patients/ | Get My Patients |
| GET | /api/patients/{id}/ | Get Patient |
| PUT | /api/patients/{id}/ | Update Patient |
| DELETE | /api/patients/{id}/ | Delete Patient |

---

# Patient-Doctor Mapping APIs

| Method | Endpoint | Description |
|----------|----------|----------|
| POST | /api/mappings/ | Assign Doctor |
| GET | /api/mappings/ | Get All Mappings |
| GET | /api/mappings/{patient_id}/ | Get Patient Doctors |
| DELETE | /api/mappings/delete/{id}/ | Remove Mapping |

---

# Authentication

All APIs except Register and Login require JWT Authentication.

Authorization Header:

```text
Bearer <access_token>
```

---

# Testing

The project was tested using Postman.

Import the included Postman Collection to test all APIs.

---

# Author

Dilawar Ahmad
