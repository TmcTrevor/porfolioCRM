from pydantic import BaseModel
from typing import List
from app.schemas.experience.base import Experience


class ExperienceList(BaseModel):
    items: List[Experience]
    page: int
    limit: int
    total: int