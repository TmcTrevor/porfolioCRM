from pydantic import BaseModel
from typing import List, Optional

from app.schemas.project.base import (
    ProjectType,
    ProjectImage,
    ProjectCTA,
    ProjectLink,
)


class ProjectCreate(BaseModel):
    type: ProjectType
    title: str
    subtitle_tag: str
    role: str
    highlight: str
    description: str
    image: ProjectImage
    tech: List[str]
    cta: ProjectCTA
    links: Optional[List[ProjectLink]] = None