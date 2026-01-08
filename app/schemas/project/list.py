from pydantic import BaseModel
from typing import List
from app.schemas.project.base import Project


class ProjectList(BaseModel):
    items: List[Project]
    page: int
    limit: int
    total: int