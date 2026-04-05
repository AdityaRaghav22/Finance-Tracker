# Finance Records API

A **Flask-based REST API** for managing financial records with **JWT authentication, role-based access control (RBAC), and analytics dashboard endpoints**.

This API allows users to securely manage income and expense records while providing role-based access to analytics and user management.

---

# Features

### Authentication

* User registration
* Secure login with JWT
* Password hashing with Bcrypt

### Role-Based Access Control

Roles supported:

* **Admin**
* **Analyst**
* **User**

Access control implemented using custom decorators.

### User Management

* Get user details
* List users
* Update user information
* Soft delete users

### Financial Records

* Create financial records
* Update financial records
* Soft delete records
* List records by user
* Filter records by date

### Dashboard Analytics

* Total income
* Total expense
* Balance
* Monthly income/expense analytics
* Category-wise analytics

---

# Tech Stack

| Technology          | Purpose           |
| ------------------- | ----------------- |
| Flask               | Web framework     |
| SQLAlchemy          | ORM               |
| Flask-JWT-Extended  | Authentication    |
| Flask-Bcrypt        | Password hashing  |
| Flasgger            | API documentation |
| SQLite / PostgreSQL | Database          |

---

# Project Structure

```
finance_project
│
├── app
│   ├── model
│   │   ├── user.py
│   │   └── financial_record.py
│   │
│   ├── routes
│   │   ├── auth.py
│   │   ├── user.py
│   │   ├── frecord.py
│   │   └── dashboard.py
│   │
│   ├── service
│   │   ├── auth_service.py
│   │   ├── frecord_service.py
│   │   └── dashboard_service.py
│   │
│   └── utils
│       ├── auth_validators.py
│       ├── frecord_validators.py
│       └── decorators.py
│
├── extensions.py
├── migrations
├── instance
├── config.py
├── app.py
├── requirements.txt
└── README.md
```

Environment Variables
---

# This project uses a .env file to store sensitive configuration such as the database connection string and JWT secret key.

## Create a .env file in the project root directory.

---
```
Example .env
FLASK_APP=app.py
FLASK_ENV=development

SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret_key

DATABASE_URL=sqlite:///finance.db
```
---

# Installation

## Clone the repository

```
git clone https://github.com/yourusername/finance-records-api.git
cd finance-records-api
```

---

## Create virtual environment

```
python -m venv venv
```

Activate it:

### Windows

```
venv\Scripts\activate
```

### Linux / Mac

```
source venv/bin/activate
```

---

## Install dependencies

```
pip install -r requirements.txt
```

---

# Run the Application

```
python app.py
```

Server runs at:

```
http://localhost:5000
```

---

# API Documentation

Interactive Swagger documentation available at:


https://adityaraghav22-6426835.postman.co/workspace/Aditya-Raghav's-Workspace~6397efc7-5300-43ff-8331-aa42feae6d9a/collection/49375862-1c7d90f8-7a26-4b39-95a5-844ded7616b6?action=share&creator=49375862```

# API Endpoints

## Authentication

| Method | Endpoint | Description |
|------|------|------|
| POST | /auth/register | Register a new user |
| POST | /auth/login | Login and receive JWT token |

---

## Users

| Method | Endpoint | Description |
|------|------|------|
| GET | /users | Get all users |
| GET | /users/<id> | Get user details |
| PUT | /users/<id> | Update user |
| DELETE | /users/<id> | Soft delete user |

---

## Financial Records

| Method | Endpoint | Description |
|------|------|------|
| POST | /frecord | Create financial record |
| GET | /frecord/<id> | Get record |
| PUT | /frecord/<id> | Update record |
| DELETE | /frecord/<id> | Soft delete record |
| GET | /frecord/user/<user_id> | Get user records |

---

## Dashboard

| Method | Endpoint | Description |
|------|------|------|
| GET | /dashboard/summary/<user_id> | Income / Expense summary |
| GET | /dashboard/monthly/<user_id> | Monthly analytics |
| GET | /dashboard/category/<user_id> | Category analytics |

---

# Role Permissions

| Role    | Access             |
| ------- | ------------------ |
| Admin   | Full system access |
| Analyst | Access analytics   |
| User    | Manage own records |

---

# Future Improvements

* Pagination for large datasets
* Refresh token authentication
* Docker containerization
* CI/CD pipeline
* Unit testing
* Multi-tenant architecture

---

# Author

**Aditya Raghav**

Backend project demonstrating:

* Flask API architecture
* JWT authentication
* Role-based access control
* Financial data analytics
