from typing import Optional
from pydantic import BaseModel

from app.schemas.common import Image, SkillCategory, SkillLevel, SkillTier


class Skill(BaseModel):
    name : str
    category : SkillCategory
    skillTier : SkillTier
    skillLevel : SkillLevel
    icon : Optional[Image] = None

