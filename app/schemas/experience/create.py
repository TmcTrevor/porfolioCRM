from pydantic import BaseModel
from typing import List, Optional

from app.schemas.experience.base import RoleType, KeyImpactTone, BulletGroup


class ExperienceCreate(BaseModel):
    date_label: str
    title: str
    company: str
    role_type: RoleType

    key_impact_icon: str
    key_impact_tone: KeyImpactTone
    key_impact: str

    groups: Optional[List[BulletGroup]] = None
    bullets: Optional[List[str]] = None