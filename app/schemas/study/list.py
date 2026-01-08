from pydantic import BaseModel
from typing import List
from app.schemas.study.base import Academic


class AcademicList(BaseModel):
    items: List[Academic]
    page: int
    limit: int
    total: int