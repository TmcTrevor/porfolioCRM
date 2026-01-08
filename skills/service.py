from typing import List

from skills.schemas import Skill, SkillList
from shared.common import SkillLevel, SkillTier, SkillCategory


MOCK_SKILLS: List[Skill] = [
    Skill(name="React", category=SkillCategory.frontEnd, skillTier=SkillTier.main, skillLevel=SkillLevel.expert),
    Skill(name="TypeScript", category=SkillCategory.frontEnd, skillTier=SkillTier.main, skillLevel=SkillLevel.expert),
    Skill(name="FastAPI", category=SkillCategory.backend, skillTier=SkillTier.main, skillLevel=SkillLevel.comfortable),
    Skill(name="PostgreSQL", category=SkillCategory.database_data, skillTier=SkillTier.main, skillLevel=SkillLevel.strong),
    Skill(name="Docker", category=SkillCategory.devops_cloud, skillTier=SkillTier.main, skillLevel=SkillLevel.strong),
    Skill(name="AWS", category=SkillCategory.devops_cloud, skillTier=SkillTier.learning, skillLevel=SkillLevel.learning),
]


async def get_skills(page: int = 1, limit: int = 50) -> SkillList:
    # simple pagination over the mock list
    start = (page - 1) * limit
    end = start + limit

    items = MOCK_SKILLS[start:end]

    return SkillList(
        skills=items,
        page=page,
        limit=limit,
        total=len(MOCK_SKILLS),
    )


async def add_skill(skill: Skill) -> Skill:
    MOCK_SKILLS.append(skill)
    return skill


async def update_skill(skill_name: str, new_skill: Skill) -> Skill:
    for i, s in enumerate(MOCK_SKILLS):
        if s.name.lower() == skill_name.lower():
            MOCK_SKILLS[i] = new_skill
            return new_skill
    raise KeyError("Skill not found")


async def delete_skill(skill_name: str) -> None:
    for i, s in enumerate(MOCK_SKILLS):
        if s.name.lower() == skill_name.lower():
            MOCK_SKILLS.pop(i)
            return
    raise KeyError("Skill not found")
