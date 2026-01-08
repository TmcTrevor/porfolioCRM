from fastapi import APIRouter
from app.api.v1.routes import healty
from app.api.v1.routes import academicStudy
from app.api.v1.routes import skills


mainRouter = APIRouter()


mainRouter.include_router(healty.router ,prefix="/healthy",tags=["healtCheck"])
mainRouter.include_router(academicStudy.router ,prefix="/study",tags=["study"])
mainRouter.include_router(skills.router,prefix="/skills", tags=["skills"])