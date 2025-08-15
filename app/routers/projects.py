from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..database import SessionLocal

router = APIRouter(prefix="/projects", tags=["Projects"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.Project])
def list_projects(db: Session = Depends(get_db)):
    return crud.get_projects(db)

@router.post("/", response_model=schemas.Project)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    return crud.create_project(db, project)
