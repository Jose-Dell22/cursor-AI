from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

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

Base = declarative_base()

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    thumbnail = Column(String)
    slug = Column(String, unique=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = Column(DateTime, nullable=True)
    teacher_id = Column(Integer, nullable=True) 