from typing import Optional
from pydantic import BaseModel


class AcademicUpdate(BaseModel):
    date_label: Optional[str] = None
    degree: Optional[str] = None
    school: Optional[str] = None
    icon: Optional[str] = None

    badge: Optional[str] = None
    note: Optional[str] = None