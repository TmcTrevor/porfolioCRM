from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, HttpUrl


class ProjectLinkKind(str, Enum):
    github = "github"
    live = "live"


class ProjectLink(BaseModel):
    kind: ProjectLinkKind
    href: str


class ProjectType(str, Enum):
    featured = "featured"
    compact = "compact"


class ProjectImage(BaseModel):
    src: str
    alt: str


class ProjectCTA(BaseModel):
    label: str
    on_click_href: Optional[str] = None


class Project(BaseModel):
    id: str
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