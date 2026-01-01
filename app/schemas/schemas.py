from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


# Customer Schemas
class CustomerBase(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    company: Optional[str] = None
    address: Optional[str] = None


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    company: Optional[str] = None
    address: Optional[str] = None


class Customer(CustomerBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# Contact Schemas
class ContactBase(BaseModel):
    customer_id: int
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    position: Optional[str] = None
    notes: Optional[str] = None


class ContactCreate(ContactBase):
    pass


class ContactUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    position: Optional[str] = None
    notes: Optional[str] = None


class Contact(ContactBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# Deal Schemas
class DealBase(BaseModel):
    customer_id: int
    title: str
    description: Optional[str] = None
    value: Optional[float] = 0.0
    status: Optional[str] = "new"
    stage: Optional[str] = "prospecting"
    expected_close_date: Optional[datetime] = None


class DealCreate(DealBase):
    pass


class DealUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    value: Optional[float] = None
    status: Optional[str] = None
    stage: Optional[str] = None
    expected_close_date: Optional[datetime] = None


class Deal(DealBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# Activity Schemas
class ActivityBase(BaseModel):
    customer_id: int
    deal_id: Optional[int] = None
    activity_type: str
    subject: str
    description: Optional[str] = None
    completed: Optional[int] = 0
    due_date: Optional[datetime] = None


class ActivityCreate(ActivityBase):
    pass


class ActivityUpdate(BaseModel):
    activity_type: Optional[str] = None
    subject: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[int] = None
    due_date: Optional[datetime] = None


class Activity(ActivityBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
