from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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
                description="Curso base de matemáticas para nivelar conocimientos.",
                thumbnail="/Fundamentos_matemáticas.webp",
                slug="fundamentos-matematicas",
                teacher_id=1
            ),
            Course(
                name="Cálculo diferencial",
                description="Aprende los conceptos básicos de cálculo diferencial.",
                thumbnail="/calculo_difrencial.webp",
                slug="calculo-diferencial",
                teacher_id=1
            ),
            Course(
                name="Cálculo Integral",
                description="Domina la integral y sus aplicaciones.",
                thumbnail="/calculo_integral.webp",
                slug="calculo-integral",
                teacher_id=1
            ),
            Course(
                name="Front end programación web",
                description="Introducción al desarrollo web moderno.",
                thumbnail="/frontend_y_fundamentos_programación.webp",
                slug="frontend-programacion-web",
                teacher_id=1
            ),
            Course(
                name="Fundamentos de programación",
                description="Lógica y bases de la programación.",
                thumbnail="/frontend_y_fundamentos_programación.webp",
                slug="fundamentos-programacion",
                teacher_id=1
            ),
            Course(
                name="Trabajos de otras materias",
                description="Apoyo en tareas y proyectos universitarios.",
                thumbnail="/trabajos_otras_materias.webp",
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

# Habilitar CORS para permitir peticiones desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # O puedes poner ["http://localhost:3000"] para mayor seguridad
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
