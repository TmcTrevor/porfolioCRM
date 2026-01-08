from typing import Optional, List
from pydantic import BaseModel

from shared.common import Image, SkillCategory, SkillLevel, SkillTier


class Skill(BaseModel):
    name: str
    category: SkillCategory
    skillTier: SkillTier
    skillLevel: SkillLevel
    icon: Optional[Image] = None


class CreateSkill(BaseModel):
    name: str
    category: SkillCategory
    skillTier: SkillTier
    skillLevel: SkillLevel
    icon: Optional[Image]


class SkillList(BaseModel):
    skills: List[Skill]
    page: int
    limit: int
    total: int
