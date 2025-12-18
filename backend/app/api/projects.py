from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.models.project_schema import ProjectCreate, ProjectOut
from app.core.deps import get_db
from app.services import project_service

router = APIRouter(prefix="/projects", tags=["Projects"])

@router.post("/", response_model = ProjectOut)
def create_project(
    project: ProjectCreate, 
    db: Session = Depends(get_db)
):
    try:
        return project_service.create_project(db, project)
    except ValueError as e:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail=str(e)
        )

@router.get("/", response_model = list[ProjectOut])
def list_projects(db:Session = Depends(get_db)):
    return project_service.list_projects(db)