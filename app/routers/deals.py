from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.models import Deal, Customer
from app.schemas.schemas import Deal as DealSchema, DealCreate, DealUpdate

router = APIRouter()


@router.get("/", response_model=List[DealSchema])
def get_deals(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all deals"""
    deals = db.query(Deal).offset(skip).limit(limit).all()
    return deals


@router.get("/{deal_id}", response_model=DealSchema)
def get_deal(deal_id: int, db: Session = Depends(get_db)):
    """Get a specific deal by ID"""
    deal = db.query(Deal).filter(Deal.id == deal_id).first()
    if deal is None:
        raise HTTPException(status_code=404, detail="Deal not found")
    return deal


@router.post("/", response_model=DealSchema, status_code=201)
def create_deal(deal: DealCreate, db: Session = Depends(get_db)):
    """Create a new deal"""
    # Verify customer exists
    customer = db.query(Customer).filter(Customer.id == deal.customer_id).first()
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    
    db_deal = Deal(**deal.model_dump())
    db.add(db_deal)
    db.commit()
    db.refresh(db_deal)
    return db_deal


@router.put("/{deal_id}", response_model=DealSchema)
def update_deal(deal_id: int, deal: DealUpdate, db: Session = Depends(get_db)):
    """Update a deal"""
    db_deal = db.query(Deal).filter(Deal.id == deal_id).first()
    if db_deal is None:
        raise HTTPException(status_code=404, detail="Deal not found")
    
    update_data = deal.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_deal, key, value)
    
    db.commit()
    db.refresh(db_deal)
    return db_deal


@router.delete("/{deal_id}", status_code=204)
def delete_deal(deal_id: int, db: Session = Depends(get_db)):
    """Delete a deal"""
    db_deal = db.query(Deal).filter(Deal.id == deal_id).first()
    if db_deal is None:
        raise HTTPException(status_code=404, detail="Deal not found")
    
    db.delete(db_deal)
    db.commit()
    return None
