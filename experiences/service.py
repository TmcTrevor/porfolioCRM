from typing import List
from uuid import uuid4

from experiences.schemas import (
    Experience, 
    ExperienceList, 
    ExperienceCreate, 
    ExperienceUpdate,
    RoleType,
    KeyImpactTone,
    BulletGroup
)


MOCK_EXPERIENCES: List[Experience] = [
    Experience(
        id=str(uuid4()),
        date_label="2024",
        title="Frontend Engineer Intern",
        company="TickTickTrader",
        role_type=RoleType.internship,
        key_impact_icon="bolt",
        key_impact_tone=KeyImpactTone.primary,
        key_impact="Shipped production UI modules and improved UX flows.",
        bullets=[
            "Built reusable React components",
            "Integrated REST APIs and improved loading states",
            "Collaborated with backend team to define contracts",
        ],
    ),
    Experience(
        id=str(uuid4()),
        date_label="2025 – Present",
        title="Software Engineer",
        company="(Company Name)",
        role_type=RoleType.full_time,
        key_impact_icon="trending_up",
        key_impact_tone=KeyImpactTone.blue,
        key_impact="Led delivery of key features and improved reliability.",
        groups=[
            BulletGroup(
                icon="code",
                title="Core Contributions",
                bullets=[
                    "Implemented feature X end-to-end",
                    "Refactored module Y for maintainability",
                ],
            ),
            BulletGroup(
                icon="speed",
                title="Performance",
                bullets=[
                    "Reduced page load time with caching and code splitting",
                ],
            ),
        ],
    ),
]


async def get_experiences(page: int = 1, limit: int = 20) -> ExperienceList:
    start = (page - 1) * limit
    end = start + limit
    items = MOCK_EXPERIENCES[start:end]

    return ExperienceList(
        items=items,
        page=page,
        limit=limit,
        total=len(MOCK_EXPERIENCES),
    )


async def add_experience(payload: ExperienceCreate) -> Experience:
    exp = Experience(
        id=str(uuid4()),
        **payload.dict(),
    )
    MOCK_EXPERIENCES.append(exp)
    return exp


async def update_experience(experience_id: str, payload: ExperienceUpdate) -> Experience:
    for i, e in enumerate(MOCK_EXPERIENCES):
        if e.id == experience_id:
            updated = e.copy(update=payload.dict(exclude_unset=True))
            MOCK_EXPERIENCES[i] = updated
            return updated
    raise KeyError("Experience not found")


async def delete_experience(experience_id: str) -> None:
    for i, e in enumerate(MOCK_EXPERIENCES):
        if e.id == experience_id:
            MOCK_EXPERIENCES.pop(i)
            return
    raise KeyError("Experience not found")
