from typing import Optional, List
from pydantic import BaseModel


class Academic(BaseModel):
    id: str
    date_label: str
    degree: str
    school: str
    icon: str

    badge: Optional[str] = None
    note: Optional[str] = None


class AcademicCreate(BaseModel):
    date_label: str
    degree: str
    school: str
    icon: str

    badge: Optional[str] = None
    note: Optional[str] = None


class AcademicUpdate(BaseModel):
    date_label: Optional[str] = None
    degree: Optional[str] = None
    school: Optional[str] = None
    icon: Optional[str] = None

    badge: Optional[str] = None
    note: Optional[str] = None


class AcademicList(BaseModel):
    items: List[Academic]
    page: int
    limit: int
    total: int
