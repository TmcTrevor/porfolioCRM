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


class ProjectList(BaseModel):
    items: List[Project]
    page: int
    limit: int
    total: int
