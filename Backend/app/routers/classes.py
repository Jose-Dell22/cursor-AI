from fastapi import APIRouter, HTTPException
from typing import List
from app.models import Class
from pydantic import BaseModel

router = APIRouter(prefix="/classes", tags=["classes"])

def get_initial_classes():
    return [
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

classes_db = get_initial_classes()

class ClassCreate(BaseModel):
    course_id: int
    name: str
    description: str
    slug: str
    video_url: str

class ClassUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    slug: str | None = None
    video_url: str | None = None

@router.get("/", response_model=List[Class])
def list_classes() -> List[Class]:
    return classes_db

@router.get("/{class_id}", response_model=Class)
def get_class(class_id: int) -> Class:
    for c in classes_db:
        if c.id == class_id:
            return c
    raise HTTPException(status_code=404, detail="Class not found")

@router.post("/", response_model=Class, status_code=201)
def create_class(class_: ClassCreate) -> Class:
    new_id = max((c.id for c in classes_db), default=0) + 1
    new_class = Class.model_validate({
        **class_.model_dump(),
        "id": new_id,
        "created_at": "2021-01-01",
        "updated_at": "2021-01-01",
        "deleted_at": None
    })
    classes_db.append(new_class)
    return new_class

@router.put("/{class_id}", response_model=Class)
def update_class(class_id: int, class_update: ClassUpdate) -> Class:
    for idx, c in enumerate(classes_db):
        if c.id == class_id:
            updated_data = c.model_dump()
            update_fields = class_update.model_dump(exclude_unset=True)
            updated_data.update(update_fields)
            updated_data["updated_at"] = "2021-01-01"
            updated_class = Class.model_validate(updated_data)
            classes_db[idx] = updated_class
            return updated_class
    raise HTTPException(status_code=404, detail="Class not found")

@router.delete("/{class_id}", response_model=dict)
def delete_class(class_id: int) -> dict:
    for idx, c in enumerate(classes_db):
        if c.id == class_id:
            del classes_db[idx]
            return {"message": "Class deleted"}
    raise HTTPException(status_code=404, detail="Class not found") 