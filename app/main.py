from fastapi import FastAPI
from app.routers import customers, contacts, deals, activities
from app.database import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Portfolio CRM API",
    description="A Customer Relationship Management system built with FastAPI",
    version="1.0.0",
)

# Include routers
app.include_router(customers.router, prefix="/api/v1/customers", tags=["Customers"])
app.include_router(contacts.router, prefix="/api/v1/contacts", tags=["Contacts"])
app.include_router(deals.router, prefix="/api/v1/deals", tags=["Deals"])
app.include_router(activities.router, prefix="/api/v1/activities", tags=["Activities"])


@app.get("/")
async def root():
    return {
        "message": "Welcome to Portfolio CRM API",
        "docs": "/docs",
        "redoc": "/redoc",
    }


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
