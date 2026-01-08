from typing import Optional
from pydantic import BaseModel


class AcademicCreate(BaseModel):
    date_label: str
    degree: str
    school: str
    icon: str

    badge: Optional[str] = None
    note: Optional[str] = None