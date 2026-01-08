from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.mainRouter import mainRouter
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


app.include_router(mainRouter)
@app.get("/health")
def health_check():
    return {"status": "ok"}