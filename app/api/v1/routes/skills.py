from fastapi import APIRouter, HTTPException, Query

from app.schemas.skills.list import SkillList
from app.services.skills_service import add_skill, get_skills, update_skill, delete_skill
from app.schemas.skills.base import Skill


router = APIRouter()

@router.get("", response_model=SkillList)
async def list_skills(
    page: int = Query(1, ge=1),
    limit: int = Query(50, ge=1, le=200),
) -> SkillList:
    return await get_skills(page=page, limit=limit)


@router.post("", response_model=Skill)
async def create_skill(skill: Skill) -> Skill:
    return await add_skill(skill)




@router.put("/{skill_name}", response_model=Skill)
async def modify_skill(skill_name: str, payload: Skill) -> Skill:
    """
    Replace a skill by name (simple mock approach).
    """
    try:
        return await update_skill(skill_name=skill_name, new_skill=payload)
    except KeyError:
        raise HTTPException(status_code=404, detail="Skill not found")


@router.delete("/{skill_name}")
async def remove_skill(skill_name: str):
    try:
        await delete_skill(skill_name=skill_name)
        return {"deleted": True, "skill_name": skill_name}
    except KeyError:
        raise HTTPException(status_code=404, detail="Skill not found")