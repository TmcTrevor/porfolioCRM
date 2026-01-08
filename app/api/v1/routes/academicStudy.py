from fastapi import APIRouter, Query, HTTPException

from app.schemas.study.list import AcademicList
from app.schemas.study.base import Academic
from app.schemas.study.create import AcademicCreate
from app.schemas.study.update import AcademicUpdate
from app.services.studies_services import (
    get_academics,
    add_academic,
    update_academic,
    delete_academic,
)

router = APIRouter()




@router.get("", response_model=AcademicList)
async def list_academics(
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
) -> AcademicList:
    return await get_academics(page=page, limit=limit)


@router.post("", response_model=Academic)
async def create_academic(payload: AcademicCreate) -> Academic:
    return await add_academic(payload)


@router.put("/{academic_id}", response_model=Academic)
async def modify_academic(academic_id: str, payload: AcademicUpdate) -> Academic:
    try:
        return await update_academic(academic_id, payload)
    except KeyError:
        raise HTTPException(status_code=404, detail="Academic not found")


@router.delete("/{academic_id}")
async def remove_academic(academic_id: str):
    try:
        await delete_academic(academic_id)
        return {"deleted": True, "academic_id": academic_id}
    except KeyError:
        raise HTTPException(status_code=404, detail="Academic not found")