# Portfolio CRM

A Customer Relationship Management (CRM) system built with FastAPI for portfolio demonstration.

## Features

- **Customer Management**: Create, read, update, and delete customer records
- **Contact Management**: Manage multiple contacts per customer
- **Deal Tracking**: Track sales deals with status and stage tracking
- **Activity Logging**: Log activities (calls, emails, meetings, notes, tasks) for customers and deals
- **RESTful API**: Clean REST API with automatic OpenAPI documentation
- **SQLite Database**: Lightweight database for easy deployment

## Technology Stack

- **FastAPI**: Modern, fast web framework for building APIs
- **SQLAlchemy**: SQL toolkit and ORM
- **Pydantic**: Data validation using Python type annotations
- **Uvicorn**: ASGI server for running the application
- **SQLite**: Embedded database

## Installation

1. Clone the repository:
```bash
git clone https://github.com/TmcTrevor/porfolioCRM.git
cd porfolioCRM
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the development server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the application is running, you can access:

- **Interactive API docs (Swagger UI)**: http://localhost:8000/docs
- **Alternative API docs (ReDoc)**: http://localhost:8000/redoc

## API Endpoints

### Customers
- `GET /api/v1/customers/` - List all customers
- `GET /api/v1/customers/{id}` - Get a specific customer
- `POST /api/v1/customers/` - Create a new customer
- `PUT /api/v1/customers/{id}` - Update a customer
- `DELETE /api/v1/customers/{id}` - Delete a customer

### Contacts
- `GET /api/v1/contacts/` - List all contacts
- `GET /api/v1/contacts/{id}` - Get a specific contact
- `POST /api/v1/contacts/` - Create a new contact
- `PUT /api/v1/contacts/{id}` - Update a contact
- `DELETE /api/v1/contacts/{id}` - Delete a contact

### Deals
- `GET /api/v1/deals/` - List all deals
- `GET /api/v1/deals/{id}` - Get a specific deal
- `POST /api/v1/deals/` - Create a new deal
- `PUT /api/v1/deals/{id}` - Update a deal
- `DELETE /api/v1/deals/{id}` - Delete a deal

### Activities
- `GET /api/v1/activities/` - List all activities
- `GET /api/v1/activities/{id}` - Get a specific activity
- `POST /api/v1/activities/` - Create a new activity
- `PUT /api/v1/activities/{id}` - Update an activity
- `DELETE /api/v1/activities/{id}` - Delete an activity

## Data Models

### Customer
- name, email, phone, company, address
- Relationships: contacts, deals, activities

### Contact
- name, email, phone, position, notes
- Belongs to: customer

### Deal
- title, description, value, status, stage, expected_close_date
- Belongs to: customer
- Has many: activities

### Activity
- activity_type (call, email, meeting, note, task)
- subject, description, completed, due_date
- Belongs to: customer, deal (optional)

## Example Usage

### Create a Customer
```bash
curl -X POST "http://localhost:8000/api/v1/customers/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "+1234567890",
    "company": "Acme Corp"
  }'
```

### Create a Deal
```bash
curl -X POST "http://localhost:8000/api/v1/deals/" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": 1,
    "title": "Website Redesign",
    "description": "Complete website redesign project",
    "value": 50000.00,
    "status": "in_progress",
    "stage": "proposal"
  }'
```

### Log an Activity
```bash
curl -X POST "http://localhost:8000/api/v1/activities/" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": 1,
    "deal_id": 1,
    "activity_type": "call",
    "subject": "Follow-up call",
    "description": "Discussed project requirements",
    "completed": 1
  }'
```

## Project Structure

```
porfolioCRM/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application
│   ├── database.py          # Database configuration
│   ├── models/
│   │   ├── __init__.py
│   │   └── models.py        # SQLAlchemy models
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── schemas.py       # Pydantic schemas
│   └── routers/
│       ├── __init__.py
│       ├── customers.py     # Customer endpoints
│       ├── contacts.py      # Contact endpoints
│       ├── deals.py         # Deal endpoints
│       └── activities.py    # Activity endpoints
├── requirements.txt
├── .gitignore
└── README.md
```

## License

This project is open source and available for portfolio demonstration purposes.