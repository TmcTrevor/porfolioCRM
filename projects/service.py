from typing import List
from uuid import uuid4

from projects.schemas import (
    Project,
    ProjectType,
    ProjectImage,
    ProjectCTA,
    ProjectList,
    ProjectCreate,
    ProjectUpdate,
)
from shared.common import ProjectLinkKind, ProjectLink


MOCK_PROJECTS: List[Project] = [
    Project(
        id=str(uuid4()),
        type=ProjectType.featured,
        title="Portfolio CRM",
        subtitle_tag="Analytics Platform",
        role="Fullstack Developer",
        highlight="Event-driven architecture style",
        description="A modern portfolio + CRM dashboard with a FastAPI backend and AWS deployment plan.",
        image=ProjectImage(
            src="https://example.com/project1.png",
            alt="Portfolio CRM preview",
        ),
        tech=["React", "TypeScript", "FastAPI", "PostgreSQL"],
        cta=ProjectCTA(label="View Case Study", on_click_href="/projects/portfolio-crm"),
        links=[
            ProjectLink(kind=ProjectLinkKind.github, href="https://github.com/example/repo"),
            ProjectLink(kind=ProjectLinkKind.live, href="https://example.com"),
        ],
    ),
    Project(
        id=str(uuid4()),
        type=ProjectType.compact,
        title="Admin Dashboard",
        subtitle_tag="Internal Tooling",
        role="Frontend Engineer",
        highlight="Reusable component system",
        description="Built a scalable dashboard UI with filters, tables, and charts.",
        image=ProjectImage(
            src="https://example.com/project2.png",
            alt="Admin dashboard preview",
        ),
        tech=["React", "Tailwind", "Charts"],
        cta=ProjectCTA(label="Open", on_click_href="https://example.com/demo"),
        links=None,
    ),
]


async def get_projects(page: int = 1, limit: int = 20) -> ProjectList:
    start = (page - 1) * limit
    end = start + limit
    items = MOCK_PROJECTS[start:end]

    return ProjectList(
        items=items,
        page=page,
        limit=limit,
        total=len(MOCK_PROJECTS),
    )


async def add_project(payload: ProjectCreate) -> Project:
    p = Project(id=str(uuid4()), **payload.dict())
    MOCK_PROJECTS.append(p)
    return p


async def update_project(project_id: str, payload: ProjectUpdate) -> Project:
    for i, p in enumerate(MOCK_PROJECTS):
        if p.id == project_id:
            updated = p.copy(update=payload.dict(exclude_unset=True))
            MOCK_PROJECTS[i] = updated
            return updated
    raise KeyError("Project not found")


async def delete_project(project_id: str) -> None:
    for i, p in enumerate(MOCK_PROJECTS):
        if p.id == project_id:
            MOCK_PROJECTS.pop(i)
            return
    raise KeyError("Project not found")
