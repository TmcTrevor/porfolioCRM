# Portfolio CRM API

A modern portfolio and CRM backend API built with FastAPI, following a feature-based architecture pattern.

## 🏗️ Project Structure

The project follows a **feature-based architecture**, where each feature/domain has its own module with all related components:

```
porfolioCRM/
├── app/                      # Main application module
│   ├── main.py              # FastAPI application setup and routing
│   ├── config.py            # Application configuration
│   └── dependencies.py      # Dependency injection
│
├── core/                     # Core/shared utilities
│   ├── database.py          # Database configuration (placeholder)
│   ├── security.py          # Security utilities (placeholder)
│   └── exceptions.py        # Custom exceptions (placeholder)
│
├── shared/                   # Shared domain logic
│   ├── common.py            # Common schemas (enums, base models)
│   └── pagination.py        # Pagination utilities
│
├── studies/                  # Academic studies feature
│   ├── router.py            # API endpoints
│   ├── service.py           # Business logic
│   └── schemas.py           # Pydantic models
│
├── skills/                   # Skills feature
│   ├── router.py            # API endpoints
│   ├── service.py           # Business logic
│   └── schemas.py           # Pydantic models
│
├── experiences/              # Work experiences feature
│   ├── router.py            # API endpoints
│   ├── service.py           # Business logic
│   └── schemas.py           # Pydantic models
│
├── projects/                 # Projects feature
│   ├── router.py            # API endpoints
│   ├── service.py           # Business logic
│   └── schemas.py           # Pydantic models
│
└── requirements.txt          # Python dependencies
```

## 🚀 Getting Started

### Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Server

Start the development server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

### API Documentation

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 📚 API Endpoints

- **Health Check**: `GET /health`, `GET /healthy`
- **Studies**: `GET /study`, `POST /study`, `PUT /study/{id}`, `DELETE /study/{id}`
- **Skills**: `GET /skills`, `POST /skills`, `PUT /skills/{name}`, `DELETE /skills/{name}`
- **Experiences**: `GET /experiences`, `POST /experiences`, `PUT /experiences/{id}`, `DELETE /experiences/{id}`
- **Projects**: `GET /projects`, `POST /projects`, `PUT /projects/{id}`, `DELETE /projects/{id}`

## 🏛️ Architecture Pattern

This project uses a **feature-based (vertical slice) architecture** where:

- Each feature is self-contained in its own module
- Features have their own router, service, and schemas
- Shared code lives in `shared/` and `core/`
- The `app/` directory contains only the application entry point and configuration

This structure makes it easy to:
- Find all code related to a feature in one place
- Add new features without touching existing code
- Test features independently
- Scale the codebase as it grows