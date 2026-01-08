from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from studies.router import router as studies_router
from skills.router import router as skills_router
from experiences.router import router as experiences_router
from projects.router import router as projects_router

app = FastAPI(
    title="Portfolio API",
    version="0.1.0",
)

# CORS (allow React dev server)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:5173",  # Vite
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include feature routers
app.include_router(studies_router, prefix="/study", tags=["study"])
app.include_router(skills_router, prefix="/skills", tags=["skills"])
app.include_router(experiences_router, prefix="/experiences", tags=["experiences"])
app.include_router(projects_router, prefix="/projects", tags=["projects"])


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/healthy")
def healthy_check():
    return {"status": "healthy"}
