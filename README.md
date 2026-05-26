# E-Commerce Backend API

A production-style E-Commerce Backend built using FastAPI, PostgreSQL, JWT Authentication, and raw SQL queries.

This project demonstrates backend engineering fundamentals including:

- Authentication & Authorization
- JWT Token Handling
- Role-Based Access Control
- Product Management
- Order & Cart Management
- PostgreSQL Integration
- Clean Architecture
- Request Validation
- Error Handling
- Logging

---

# Tech Stack

- FastAPI
- PostgreSQL
- psycopg2
- JWT Authentication
- bcrypt Password Hashing
- Pydantic Validation

---

# Project Structure

```bash
app/
│
├── main.py
├── config.py
├── database.py
│
├── routes/
│   ├── auth_routes.py
│   ├── product_routes.py
│   ├── order_routes.py
│   └── cart_routes.py
│
├── services/
├── repositories/
├── schemas/
├── middleware/
├── utils/
└── logs/
```

---

# Features

## Authentication
- User Registration
- User Login
- JWT Authentication
- Protected Routes
- Role-Based Authorization

## Products
- Add Product
- Get Products
- Update Product
- Delete Product
- Pagination Support

## Orders
- Place Orders
- View User Orders
- Update Order Address
- Delete Orders

## Cart
- Add to Cart
- Get Cart Items
- Remove Cart Items

---

# Requirements

- Python 3.10+
- PostgreSQL

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/ecommerce_backend

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=60
```

---

# Installation

## Clone Repository

```bash
git clone <repository_url>

cd ecommerce_backend
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

# Run Application

Start the server:

```bash
uvicorn app.main:app --reload
```

Application runs at:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

ReDoc Documentation:

```text
http://127.0.0.1:8000/redoc
```

---

# Authentication

Protected routes require:

```text
Authorization: Bearer <access_token>
```

Example:

```text
Authorization: Bearer eyJhbGciOi...
```

---

# API Endpoints

# Authentication

| Method | Endpoint | Description |
|---|---|---|
| POST | `/auth/register` | Register new user |
| POST | `/auth/login` | Login user |
| GET | `/auth/me` | Get current user |

---

# Products

| Method | Endpoint | Description |
|---|---|---|
| POST | `/products` | Create product (Admin) |
| GET | `/products` | Get all products |
| GET | `/products/{product_id}` | Get product by ID |
| PUT | `/products/{product_id}` | Update product |
| PATCH | `/products/{product_id}` | Partial update |
| DELETE | `/products/{product_id}` | Delete product |

---

# Orders

| Method | Endpoint | Description |
|---|---|---|
| POST | `/orders/me` | Create order |
| GET | `/orders/me` | Get user orders |
| GET | `/orders/{order_id}` | Get order details |
| PATCH | `/orders/{order_id}` | Update address |
| DELETE | `/orders/{order_id}` | Delete order |

---

# Cart

| Method | Endpoint | Description |
|---|---|---|
| POST | `/cart` | Add to cart |
| GET | `/cart` | Get cart items |
| DELETE | `/cart/{order_id}` | Remove cart item |

---

# Security Features

- bcrypt Password Hashing
- JWT Authentication
- Role-Based Authorization
- Protected Routes
- Environment Variable Configuration
- Input Validation
- Secure Error Handling

---

# Logging

Application logs are stored inside:

```text
app/logs/
```

Logging includes:
- Authentication Events
- Errors
- Warnings
- API Operations

---

# Architecture

The project follows layered backend architecture:

```text
Routes
  ↓
Services
  ↓
Repositories
  ↓
Database
```This improves:
- scalability
- maintainability
- code organization
- testability

---

# Author
Kumaresan K