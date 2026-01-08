from typing import List
from uuid import uuid4

from app.schemas.study.base import Academic
from app.schemas.study.list import AcademicList
from app.schemas.study.create import AcademicCreate
from app.schemas.study.update import AcademicUpdate


MOCK_ACADEMICS: List[Academic] = [
    Academic(
        id=str(uuid4()),
        date_label="2020 – 2023",
        degree="Software Engineering",
        school="1337 Coding School",
        badge="42 Network",
        note="Project-based peer learning",
        icon="school",
    ),
    Academic(
        id=str(uuid4()),
        date_label="2017 – 2020",
        degree="Engineering Degree",
        school="ENSA",
        note="Computer Science",
        icon="school",
    ),
]


async def get_academics(page: int = 1, limit: int = 20) -> AcademicList:
    start = (page - 1) * limit
    end = start + limit

    items = MOCK_ACADEMICS[start:end]

    return AcademicList(
        items=items,
        page=page,
        limit=limit,
        total=len(MOCK_ACADEMICS),
    )

async def add_academic(payload: AcademicCreate) -> Academic:
    academic = Academic(
        id=str(uuid4()),
        **payload.dict(),
    )
    MOCK_ACADEMICS.append(academic)
    return academic

async def update_academic(academic_id: str, payload: AcademicUpdate) -> Academic:
    for i, a in enumerate(MOCK_ACADEMICS):
        if a.id == academic_id:
            updated = a.copy(update=payload.dict(exclude_unset=True))
            MOCK_ACADEMICS[i] = updated
            return updated
    raise KeyError("Academic not found")

async def delete_academic(academic_id: str) -> None:
    for i, a in enumerate(MOCK_ACADEMICS):
        if a.id == academic_id:
            MOCK_ACADEMICS.pop(i)
            return
    raise KeyError("Academic not found")