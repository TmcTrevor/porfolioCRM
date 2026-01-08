from fastapi import APIRouter, Query, HTTPException

from experiences.schemas import ExperienceList, Experience, ExperienceCreate, ExperienceUpdate
from experiences.service import (
    get_experiences,
    add_experience,
    update_experience,
    delete_experience,
)

router = APIRouter()


@router.get("", response_model=ExperienceList)
async def list_experiences(
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
) -> ExperienceList:
    return await get_experiences(page=page, limit=limit)


@router.post("", response_model=Experience)
async def create_experience(payload: ExperienceCreate) -> Experience:
    return await add_experience(payload)


@router.put("/{experience_id}", response_model=Experience)
async def modify_experience(experience_id: str, payload: ExperienceUpdate) -> Experience:
    try:
        return await update_experience(experience_id, payload)
    except KeyError:
        raise HTTPException(status_code=404, detail="Experience not found")


@router.delete("/{experience_id}")
async def remove_experience(experience_id: str):
    try:
        await delete_experience(experience_id)
        return {"deleted": True, "experience_id": experience_id}
    except KeyError:
        raise HTTPException(status_code=404, detail="Experience not found")
