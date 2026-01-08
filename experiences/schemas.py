from enum import Enum
from typing import List, Optional
from pydantic import BaseModel


class RoleType(str, Enum):
    full_time = "Full-time"
    internship = "Internship"
    part_time = "Part-time"


class KeyImpactTone(str, Enum):
    primary = "primary"
    blue = "blue"
    muted = "muted"


class BulletGroup(BaseModel):
    icon: str
    title: str
    bullets: List[str]


class Experience(BaseModel):
    id: str
    date_label: str
    title: str
    company: str
    role_type: RoleType

    key_impact_icon: str
    key_impact_tone: KeyImpactTone
    key_impact: str  # send as text/markdown (NOT ReactNode)

    groups: Optional[List[BulletGroup]] = None
    bullets: Optional[List[str]] = None


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


class ExperienceList(BaseModel):
    items: List[Experience]
    page: int
    limit: int
    total: int
