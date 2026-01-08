from pydantic import BaseModel
from typing import List, Optional

from app.schemas.project.base import (
    ProjectType,
    ProjectImage,
    ProjectCTA,
    ProjectLink,
)


class ProjectUpdate(BaseModel):
    type: Optional[ProjectType] = None
    title: Optional[str] = None
    subtitle_tag: Optional[str] = None
    role: Optional[str] = None
    highlight: Optional[str] = None
    description: Optional[str] = None
    image: Optional[ProjectImage] = None
    tech: Optional[List[str]] = None
    cta: Optional[ProjectCTA] = None
    links: Optional[List[ProjectLink]] = None