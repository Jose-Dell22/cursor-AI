from fastapi import FastAPI
from app.core.config import Settings
from app.routers.courses import router as courses_router
from app.routers.teachers import router as teachers_router
from app.routers.classes import router as classes_router

settings = Settings()

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

app.include_router(courses_router)
app.include_router(teachers_router)
app.include_router(classes_router)

@app.get("/", response_model=dict)
def root() -> dict:
    return {"message": "Bienvenido a Platziflix API"}

@app.get("/health", response_model=dict)
def health() -> dict:
    return {
        "status": "ok",
        "service": settings.PROJECT_NAME,
        "version": settings.VERSION
    }
