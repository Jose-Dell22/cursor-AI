from fastapi import APIRouter, HTTPException
from typing import List
from app.models import Teacher
from pydantic import BaseModel

router = APIRouter(prefix="/teachers", tags=["teachers"])

def get_initial_teachers():
    return [
        Teacher.model_validate({
            "id": 1,
            "name": "John Doe",
            "email": "john.doe@example.com",
            "created_at": "2021-01-01",
            "updated_at": "2021-01-01",
            "deleted_at": None
        })
    ]

teachers_db = get_initial_teachers()

class TeacherCreate(BaseModel):
    name: str
    email: str

class TeacherUpdate(BaseModel):
    name: str | None = None
    email: str | None = None

@router.get("/", response_model=List[Teacher])
def list_teachers() -> List[Teacher]:
    return teachers_db

@router.get("/{teacher_id}", response_model=Teacher)
def get_teacher(teacher_id: int) -> Teacher:
    for teacher in teachers_db:
        if teacher.id == teacher_id:
            return teacher
    raise HTTPException(status_code=404, detail="Teacher not found")

@router.post("/", response_model=Teacher, status_code=201)
def create_teacher(teacher: TeacherCreate) -> Teacher:
    new_id = max((t.id for t in teachers_db), default=0) + 1
    new_teacher = Teacher.model_validate({
        **teacher.model_dump(),
        "id": new_id,
        "created_at": "2021-01-01",
        "updated_at": "2021-01-01",
        "deleted_at": None
    })
    teachers_db.append(new_teacher)
    return new_teacher

@router.put("/{teacher_id}", response_model=Teacher)
def update_teacher(teacher_id: int, teacher_update: TeacherUpdate) -> Teacher:
    for idx, teacher in enumerate(teachers_db):
        if teacher.id == teacher_id:
            updated_data = teacher.model_dump()
            update_fields = teacher_update.model_dump(exclude_unset=True)
            updated_data.update(update_fields)
            updated_data["updated_at"] = "2021-01-01"
            updated_teacher = Teacher.model_validate(updated_data)
            teachers_db[idx] = updated_teacher
            return updated_teacher
    raise HTTPException(status_code=404, detail="Teacher not found")

@router.delete("/{teacher_id}", response_model=dict)
def delete_teacher(teacher_id: int) -> dict:
    for idx, teacher in enumerate(teachers_db):
        if teacher.id == teacher_id:
            del teachers_db[idx]
            return {"message": "Teacher deleted"}
    raise HTTPException(status_code=404, detail="Teacher not found") 