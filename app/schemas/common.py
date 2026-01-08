from enum import Enum
from pydantic import BaseModel, HttpUrl
from enum import Enum


class ProjectLinkKind(str, Enum):
    github = "github"
    live = "live"


class ProjectLink(BaseModel):
    kind: ProjectLinkKind
    href: HttpUrl


class Image(BaseModel):
    src: HttpUrl
    alt: str


class SkillCategory(str, Enum):
    frontEnd = "frontEnd"
    backend = "backend"
    devops_cloud = "devops_cloud"
    database_data = "database_data"


class SkillLevel(str, Enum):
    WorkingKnowl = "Working Knowl"
    confortable = "Confortable"
    strong = "Strong"
    expert = "Expert"
    learning = "Learning"


class SkillTier(str, Enum):
    main = "Main"
    secondary = "Secondary"
    learning = "Learning"


