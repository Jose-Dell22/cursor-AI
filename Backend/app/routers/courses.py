from fastapi import APIRouter, HTTPException
from typing import List
from app.models import Course, Class
from pydantic import BaseModel

router = APIRouter(prefix="/courses", tags=["courses"])

# Datos simulados
def get_initial_courses():
    return [
        Course.model_validate({
            "id": 1,
            "name": "Curso de React",
            "description": "Curso de React",
            "thumbnail": "https://via.placeholder.com/150",
            "slug": "curso-de-react",
            "created_at": "2021-01-01",
            "updated_at": "2021-01-01",
            "deleted_at": None,
            "teacher_id": [1, 2, 3]
        })
    ]

courses_db = get_initial_courses()

classes_db = [
    Class.model_validate({
        "id": 1,
        "course_id": 1,
        "name": "Clase 1",
        "description": "Clase 1",
        "slug": "clase-1",
        "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "created_at": "2021-01-01",
        "updated_at": "2021-01-01",
        "deleted_at": None
    })
]

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

@router.get("/", response_model=List[Course])
def list_courses() -> List[Course]:
    return courses_db

@router.get("/{slug}", response_model=Course)
def get_course(slug: str) -> Course:
    for course in courses_db:
        if course.slug == slug:
            return course
    raise HTTPException(status_code=404, detail="Course not found")

@router.post("/", response_model=Course, status_code=201)
def create_course(course: CourseCreate) -> Course:
    new_id = max((c.id for c in courses_db), default=0) + 1
    new_course = Course.model_validate({
        **course.model_dump(),
        "id": new_id,
        "created_at": "2021-01-01",
        "updated_at": "2021-01-01",
        "deleted_at": None
    })
    courses_db.append(new_course)
    return new_course

@router.put("/{slug}", response_model=Course)
def update_course(slug: str, course_update: CourseUpdate) -> Course:
    for idx, course in enumerate(courses_db):
        if course.slug == slug:
            updated_data = course.model_dump()
            update_fields = course_update.model_dump(exclude_unset=True)
            updated_data.update(update_fields)
            updated_data["updated_at"] = "2021-01-01"
            updated_course = Course.model_validate(updated_data)
            courses_db[idx] = updated_course
            return updated_course
    raise HTTPException(status_code=404, detail="Course not found")

@router.delete("/{slug}", response_model=dict)
def delete_course(slug: str) -> dict:
    for idx, course in enumerate(courses_db):
        if course.slug == slug:
            del courses_db[idx]
            return {"message": "Course deleted"}
    raise HTTPException(status_code=404, detail="Course not found")

@router.get("/{slug}/classes/{class_id}", response_model=Class)
def get_class(slug: str, class_id: int) -> Class:
    for course in courses_db:
        if course.slug == slug:
            for c in classes_db:
                if c.id == class_id and c.course_id == course.id:
                    return c
    raise HTTPException(status_code=404, detail="Class not found") 