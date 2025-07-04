from fastapi import FastAPI
from app.core.config import Settings
from app.routers.courses import router as courses_router
from app.routers.teachers import router as teachers_router
from app.routers.classes import router as classes_router
from app.db import engine
from app.models import Base, Course, Teacher
from sqlalchemy.orm import Session
from datetime import datetime

settings = Settings()

# Crear tablas
Base.metadata.create_all(bind=engine)

# Insertar datos iniciales
def insert_initial_data():
    db = Session(engine)
    try:
        # Borra todos los cursos y profesores existentes
        db.query(Course).delete()
        db.query(Teacher).delete()
        db.commit()
        # Inserta el profesor
        teacher = Teacher.model_validate({
            "id": 1,
            "name": "Jose Fernando Dell",
            "email": "jfdell41@gmail.com",
            "created_at": datetime.utcnow().isoformat(),
            "updated_at": datetime.utcnow().isoformat(),
            "deleted_at": None
        })
        db.add(Teacher(**teacher.model_dump()))
        db.commit()
        # Inserta los cursos de ejemplo con teacher_id=1
        courses = [
            Course(
                name="Fundamentos en matemáticas",
                description="Asesoría y trabajos en fundamentos de matemáticas.",
                thumbnail="https://images.unsplash.com/photo-1635070041078-e363dbe005cb?auto=format&fit=crop&w=400&q=80",  # Matemáticas básicas
                slug="fundamentos-matematicas",
                teacher_id=1
            ),
            Course(
                name="Cálculo diferencial",
                description="Asesoría y trabajos en cálculo diferencial.",
                thumbnail="https://images.unsplash.com/photo-1509228468518-180dd4864904?auto=format&fit=crop&w=400&q=80",  # Cálculo diferencial
                slug="calculo-diferencial",
                teacher_id=1
            ),
            Course(
                name="Cálculo Integral",
                description="Asesoría y trabajos en cálculo integral.",
                thumbnail="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=400&q=80",  # Cálculo integral
                slug="calculo-integral",
                teacher_id=1
            ),
            Course(
                name="Front end programación web",
                description="Asesoría y trabajos en programación web.",
                thumbnail="https://images.unsplash.com/photo-1547658719-da2b51169166?auto=format&fit=crop&w=400&q=80",  # Desarrollo web frontend
                slug="frontend-programacion-web",
                teacher_id=1
            ),
            Course(
                name="Fundamentos de programación",
                description="Asesoría y trabajos en fundamentos de programación.",
                thumbnail="https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=400&q=80",  # Código de programación
                slug="fundamentos-programacion",
                teacher_id=1
            ),
            Course(
                name="Trabajos de otras materias",
                description="Asesoría y trabajos en otras materias universitarias.",
                thumbnail="https://images.unsplash.com/photo-1523050854058-8df90110c9a1?auto=format&fit=crop&w=400&q=80",  # Universidad y educación
                slug="trabajos-otras-materias",
                teacher_id=1
            ),
        ]
        db.add_all(courses)
        db.commit()
    except Exception as e:
        print(f"Error inserting initial data: {e}")
    finally:
        db.close()

# Insertar datos al iniciar
insert_initial_data()

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
