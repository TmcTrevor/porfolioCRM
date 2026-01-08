from typing import Optional
from pydantic import BaseModel


class Academic(BaseModel):
    id: str
    date_label: str
    degree: str
    school: str
    icon: str

    badge: Optional[str] = None
    note: Optional[str] = None