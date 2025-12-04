# FastAPI TodoList Application  
[![FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](#license)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)]()
[![API](https://img.shields.io/badge/API-REST-lightgrey)]()

A lightweight, modular TodoList REST API built with **FastAPI**, featuring an **in-memory store** and a clean separation of concerns between routing, business logic, and data models.

This project is intentionally minimal and ideal for:
- Learning FastAPI fundamentals  
- Interview preparation  
- Expanding into database-backed or production-grade APIs  

---

## 1. Overview

This application implements a complete set of CRUD operations for Todo items using FastAPI's declarative routing and Pydantic models.  
All Todo items are stored **in memory**, making the project simple to understand and easy to run without external dependencies.

Key design aspects include:
- Dedicated **service layer** (`service.py`)
- Clean **model** definitions (`model.py`)
- Minimal **entrypoint** router (`main.py`)
- Strict typing and Pydantic validation
- Support for full and partial updates

---

## 2. Features

- Create Todo items  
- Retrieve all or individual Todo items  
- Update and partially update items (`PUT` and `PATCH`)  
- Delete single or all todos  
- Filter completed and incomplete todos  
- Mark a todo as completed  
- Count all todos  
- Structured three-file architecture:
  - `main.py` → HTTP routing
  - `service.py` → Business logic
  - `model.py` → Data modelling

---

## 3. Project Structure

```
.
├── main.py        # FastAPI app with route declarations
├── service.py     # Business logic and in-memory operations
├── model.py       # Pydantic TodoItem model
└── README.md
```

---

## 4. Installation

### Requirements
- Python 3.10 or above

### Install Dependencies

```bash
pip install fastapi uvicorn pydantic
```

---

## 5. Running the Application

Start the API server using Uvicorn:

```bash
uvicorn main:app --reload
```

Access the application:

```
http://localhost:8000
```

### API Documentation

FastAPI provides interactive documentation out-of-the-box:

- Swagger UI: http://localhost:8000/docs  
- ReDoc: http://localhost:8000/redoc  

---

## 6. Data Model (model.py)

```python
from typing import Optional
from pydantic import BaseModel

class TodoItem(BaseModel):
    id: int
    name: str
    description: Optional[str] = "No description provided"
    completed: bool = False
```

---

## 7. Service Layer (service.py)

Business logic is separated from routing for clarity, maintainability, and testability.

Functions include:

- get_todos()
- get_todo_by_id()
- create_todo()
- update_todo_by_id()
- patch_todo_by_id()
- delete_todo_by_id()
- delete_all_todos()
- get_completed_todos()
- get_incomplete_todos()
- mark_todo_as_completed()
- todos_count()

---

## 8. API Endpoints Summary

| Method | Endpoint                     | Description                          |
|--------|-------------------------------|--------------------------------------|
| GET    | `/todos`                     | Get all todos                        |
| GET    | `/todos/{id}`                | Get a specific todo                  |
| POST   | `/todos`                     | Create a new todo                    |
| PUT    | `/todos/{id}`                | Replace entire todo                  |
| PATCH  | `/todos/{id}`                | Partially update a todo              |
| DELETE | `/todos/{id}`                | Delete specific todo                 |
| DELETE | `/todos`                     | Delete all todos                     |
| GET    | `/todos/completed`           | Get completed todos                  |
| GET    | `/todos/incomplete`          | Get incomplete todos                 |
| POST   | `/todos/{id}/complete`       | Mark todo as completed               |
| GET    | `/todos/count`               | Get total todo count                 |

---

## 9. Future Enhancements

Potential improvements:

- SQLite or PostgreSQL repository  
- SQLAlchemy ORM integration  
- Authentication with JWT  
- Pagination  
- Dockerization  
- Unit tests  

---

## 10. License

MIT License.
