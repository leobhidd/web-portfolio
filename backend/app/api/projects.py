from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.project import Project
from app.models.project_schema import ProjectCreate, ProjectOut
from app.core.deps import get_db

router = APIRouter(prefix="/projects", tags=["Projects"])

@router.post("/", response_model = ProjectOut)
def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    db_project = Project(**project.dict())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

@router.get("/", response_model = list[ProjectOut])
def list_projects(db:Session = Depends(get_db)):
    return db.query(Project).all()