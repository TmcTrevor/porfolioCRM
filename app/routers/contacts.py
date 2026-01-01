from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.models import Contact, Customer
from app.schemas.schemas import Contact as ContactSchema, ContactCreate, ContactUpdate

router = APIRouter()


@router.get("/", response_model=List[ContactSchema])
def get_contacts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all contacts"""
    contacts = db.query(Contact).offset(skip).limit(limit).all()
    return contacts


@router.get("/{contact_id}", response_model=ContactSchema)
def get_contact(contact_id: int, db: Session = Depends(get_db)):
    """Get a specific contact by ID"""
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact


@router.post("/", response_model=ContactSchema, status_code=201)
def create_contact(contact: ContactCreate, db: Session = Depends(get_db)):
    """Create a new contact"""
    # Verify customer exists
    customer = db.query(Customer).filter(Customer.id == contact.customer_id).first()
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    
    db_contact = Contact(**contact.model_dump())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact


@router.put("/{contact_id}", response_model=ContactSchema)
def update_contact(contact_id: int, contact: ContactUpdate, db: Session = Depends(get_db)):
    """Update a contact"""
    db_contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if db_contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    
    update_data = contact.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_contact, key, value)
    
    db.commit()
    db.refresh(db_contact)
    return db_contact


@router.delete("/{contact_id}", status_code=204)
def delete_contact(contact_id: int, db: Session = Depends(get_db)):
    """Delete a contact"""
    db_contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if db_contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    
    db.delete(db_contact)
    db.commit()
    return None
