from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.models import Activity, Customer, Deal
from app.schemas.schemas import Activity as ActivitySchema, ActivityCreate, ActivityUpdate

router = APIRouter()


@router.get("/", response_model=List[ActivitySchema])
def get_activities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all activities"""
    activities = db.query(Activity).offset(skip).limit(limit).all()
    return activities


@router.get("/{activity_id}", response_model=ActivitySchema)
def get_activity(activity_id: int, db: Session = Depends(get_db)):
    """Get a specific activity by ID"""
    activity = db.query(Activity).filter(Activity.id == activity_id).first()
    if activity is None:
        raise HTTPException(status_code=404, detail="Activity not found")
    return activity


@router.post("/", response_model=ActivitySchema, status_code=201)
def create_activity(activity: ActivityCreate, db: Session = Depends(get_db)):
    """Create a new activity"""
    # Verify customer exists
    customer = db.query(Customer).filter(Customer.id == activity.customer_id).first()
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    
    # Verify deal exists if provided
    if activity.deal_id:
        deal = db.query(Deal).filter(Deal.id == activity.deal_id).first()
        if deal is None:
            raise HTTPException(status_code=404, detail="Deal not found")
    
    db_activity = Activity(**activity.model_dump())
    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)
    return db_activity


@router.put("/{activity_id}", response_model=ActivitySchema)
def update_activity(activity_id: int, activity: ActivityUpdate, db: Session = Depends(get_db)):
    """Update an activity"""
    db_activity = db.query(Activity).filter(Activity.id == activity_id).first()
    if db_activity is None:
        raise HTTPException(status_code=404, detail="Activity not found")
    
    update_data = activity.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_activity, key, value)
    
    db.commit()
    db.refresh(db_activity)
    return db_activity


@router.delete("/{activity_id}", status_code=204)
def delete_activity(activity_id: int, db: Session = Depends(get_db)):
    """Delete an activity"""
    db_activity = db.query(Activity).filter(Activity.id == activity_id).first()
    if db_activity is None:
        raise HTTPException(status_code=404, detail="Activity not found")
    
    db.delete(db_activity)
    db.commit()
    return None
