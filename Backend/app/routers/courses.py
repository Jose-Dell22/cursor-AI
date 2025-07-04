from fastapi import APIRouter, Depends, HTTPException
from typing import List, Optional
from sqlalchemy.orm import Session
from app.models import Course
from app.db import get_db
from pydantic import BaseModel
from datetime import datetime

router = APIRouter(prefix="/courses", tags=["courses"])

class CourseCreate(BaseModel):
    name: str
    description: str
    thumbnail: str
    slug: str
    teacher_id: List[int]

class CourseUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    thumbnail: str | None = None
    slug: str | None = None
    teacher_id: List[int] | None = None

class CourseOut(BaseModel):
    id: int
    name: str
    description: Optional[str]
    thumbnail: Optional[str]
    slug: str
    created_at: Optional[str]
    updated_at: Optional[str]
    deleted_at: Optional[str]
    teacher_id: int

# Cursos de ejemplo en memoria
example_courses = [
    CourseOut(
        id=1,
        name="Fundamentos en matemáticas",
        description="Curso base de matemáticas para nivelar conocimientos.",
        thumbnail="/Fundamentos_matemáticas.webp",
        slug="fundamentos-matematicas",
        created_at=datetime.utcnow().isoformat(),
        updated_at=datetime.utcnow().isoformat(),
        deleted_at=None,
        teacher_id=1
    ),
    CourseOut(
        id=2,
        name="Cálculo diferencial",
        description="Aprende los conceptos básicos de cálculo diferencial.",
        thumbnail="/calculo_difrencial.webp",
        slug="calculo-diferencial",
        created_at=datetime.utcnow().isoformat(),
        updated_at=datetime.utcnow().isoformat(),
        deleted_at=None,
        teacher_id=1
    ),
    CourseOut(
        id=3,
        name="Cálculo Integral",
        description="Domina la integral y sus aplicaciones.",
        thumbnail="/calculo_integral.webp",
        slug="calculo-integral",
        created_at=datetime.utcnow().isoformat(),
        updated_at=datetime.utcnow().isoformat(),
        deleted_at=None,
        teacher_id=1
    ),
    CourseOut(
        id=4,
        name="Front end programación web",
        description="Introducción al desarrollo web moderno.",
        thumbnail="/frontend_y_fundamentos_programación.webp",
        slug="frontend-programacion-web",
        created_at=datetime.utcnow().isoformat(),
        updated_at=datetime.utcnow().isoformat(),
        deleted_at=None,
        teacher_id=1
    ),
    CourseOut(
        id=5,
        name="Fundamentos de programación",
        description="Lógica y bases de la programación.",
        thumbnail="/frontend_y_fundamentos_programación.webp",
        slug="fundamentos-programacion",
        created_at=datetime.utcnow().isoformat(),
        updated_at=datetime.utcnow().isoformat(),
        deleted_at=None,
        teacher_id=1
    ),
    CourseOut(
        id=6,
        name="Trabajos de otras materias",
        description="Apoyo en tareas y proyectos universitarios.",
        thumbnail="/trabajos_otras_materias.webp",
        slug="trabajos-otras-materias",
        created_at=datetime.utcnow().isoformat(),
        updated_at=datetime.utcnow().isoformat(),
        deleted_at=None,
        teacher_id=1
    ),
]

@router.get("/", response_model=List[CourseOut])
def list_courses() -> List[CourseOut]:
    return example_courses

@router.get("/{slug}", response_model=CourseOut)
def get_course_by_slug(slug: str):
    for course in example_courses:
        if course.slug == slug:
            return course
    raise HTTPException(status_code=404, detail="Course not found")

# El resto de las rutas (GET by slug, POST, PUT, DELETE, etc.) deben migrarse para usar la base de datos real y SQLAlchemy síncrono. 