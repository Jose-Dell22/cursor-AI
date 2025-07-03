from pydantic import BaseModel, HttpUrl
from typing import List, Optional

class Teacher(BaseModel):
    id: int
    name: str
    email: str
    created_at: str
    updated_at: str
    deleted_at: Optional[str] = None

class Class(BaseModel):
    id: int
    course_id: int
    name: str
    description: str
    slug: str
    video_url: Optional[HttpUrl] = None
    created_at: str
    updated_at: str
    deleted_at: Optional[str] = None

class Course(BaseModel):
    id: int
    name: str
    description: str
    thumbnail: HttpUrl
    slug: str
    created_at: str
    updated_at: str
    deleted_at: Optional[str] = None
    teacher_id: List[int] 