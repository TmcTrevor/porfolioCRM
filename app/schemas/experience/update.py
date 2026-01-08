from pydantic import BaseModel
from typing import List, Optional

from app.schemas.experience.base import RoleType, KeyImpactTone, BulletGroup


class ExperienceUpdate(BaseModel):
    date_label: Optional[str] = None
    title: Optional[str] = None
    company: Optional[str] = None
    role_type: Optional[RoleType] = None

    key_impact_icon: Optional[str] = None
    key_impact_tone: Optional[KeyImpactTone] = None
    key_impact: Optional[str] = None

    groups: Optional[List[BulletGroup]] = None
    bullets: Optional[List[str]] = None