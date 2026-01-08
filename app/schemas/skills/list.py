from pydantic import BaseModel
from typing import List
from app.schemas.skills.base import Skill


class SkillList(BaseModel):
    skills : List[Skill]
    page : int
    limit : int
    total : int



