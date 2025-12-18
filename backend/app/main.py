from fastapi import FastAPI
from app.api import projects
from app.core.database import engine, Base
from app.models.project import Project

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Portfolio API")

@app.get("/health")
def health():
    return {"status":"ok"}


app.include_router(projects.router)