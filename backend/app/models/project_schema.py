from pydantic import BaseModel

class ProjectBase(BaseModel):
    name: str
    description: str

class ProjectCreate(ProjectBase):
    pass

class ProjectOut(ProjectBase):
    id: int

    class Config:
        from_attributes = True