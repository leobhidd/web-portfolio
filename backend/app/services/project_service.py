from sqlalchemy.orm import Session
from app.models.project import Project
from app.models.project_schema import ProjectCreate

def create_project(db: Session, project: ProjectCreate) -> Project:
    exists = (
        db.query(Project).filter(Project.name == project.name).first()
    )
    if exists:
        raise ValueError("Project already exist")

    db_project = Project(**project.dict())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


def list_projects(db:Session = list[Project]):
    return db.query(Project).all()