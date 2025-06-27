# 📚 Book Review Service API

A simple Book Review REST API built using **FastAPI**, **SQLAlchemy**, **SQLite**, **Redis**, and **Alembic** for demonstrating API design, persistence, caching, and testing.

---

## 🔧 Features

-  CRUD operations for Books and Reviews
-  FastAPI with auto-generated Swagger/OpenAPI docs
-  Redis caching for optimized `/books` fetching
- 📦 SQLite + SQLAlchemy ORM + Alembic migrations
- ✅ Unit & Integration tests using `pytest`
- 📈 Indexed reviews for better performance

---

## 📌 Endpoints

### Books
- `GET /books` – List all books (from cache if available)
- `POST /books` – Add a new book

### Reviews
- `GET /books/{id}/reviews` – List reviews for a book
- `POST /books/{id}/reviews` – Add a review for a book

---

## 🛠 Tech Stack

- **Backend:** Python 3.11+, FastAPI
- **Database:** SQLite (can be switched to PostgreSQL easily)
- **ORM:** SQLAlchemy
- **Migrations:** Alembic
- **Cache:** Redis (with fallback to DB)
- **Testing:** Pytest

---

## Getting Started

### 1. Clone and Setup

```bash
git clone https://github.com/your-username/book-review-service.git
cd book-review-service
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
```
### 2. Run Alembic Migrations

```bash
alembic upgrade head
```
### 3. Start Redis (Skip if already running)
```bash
redis-server
```
### 4. Run the Server
```bash
uvicorn app.main:app --reload
```
Visit http://localhost:8000/docs for interactive API docs.

## ✅ Running Tests
```bash
pytest tests/
```
Covers:
- Unit tests for book & review endpoints
- Integration test for cache-miss scenario

## Author
Somesh Mishra
(Backend Developer)
