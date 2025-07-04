from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.engine import Engine
from sqlalchemy.exc import SQLAlchemyError
import os
from datetime import datetime
from app.models import Course, Teacher

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://platziflix:platziflix@localhost:5432/platziflix")

engine: Engine = create_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def insert_initial_data():
    print("Insertando datos iniciales...")
    db = SessionLocal()
    try:
        db.query(Course).delete()
        db.query(Teacher).delete()
        db.commit()
        print("Tablas limpiadas")
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
        print("Profesor insertado")
        courses = [
            # ... tus cursos aquí ...
        ]
        db.add_all(courses)
        db.commit()
        print("Cursos insertados")
    except Exception as e:
        print(f"Error inserting initial data: {e}")
    finally:
        db.close()
