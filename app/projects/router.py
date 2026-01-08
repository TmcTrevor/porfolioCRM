from fastapi import APIRouter, Query, HTTPException

from projects.schemas import Project, ProjectList, ProjectCreate, ProjectUpdate
from projects.service import (
    get_projects,
    add_project,
    update_project,
    delete_project,
)

router = APIRouter()


@router.get("", response_model=ProjectList)
async def list_projects(
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
) -> ProjectList:
    return await get_projects(page=page, limit=limit)


@router.post("", response_model=Project)
async def create_project(payload: ProjectCreate) -> Project:
    return await add_project(payload)


@router.put("/{project_id}", response_model=Project)
async def modify_project(project_id: str, payload: ProjectUpdate) -> Project:
    try:
        return await update_project(project_id, payload)
    except KeyError:
        raise HTTPException(status_code=404, detail="Project not found")


@router.delete("/{project_id}")
async def remove_project(project_id: str):
    try:
        await delete_project(project_id)
        return {"deleted": True, "project_id": project_id}
    except KeyError:
        raise HTTPException(status_code=404, detail="Project not found")
