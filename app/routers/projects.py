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


@router.get("/{id}", response_model=schemas.Project)
def get_project(id: int, db: Session = Depends(get_db)):
    return crud.get_project(db, id)


@router.put("/{id}", response_model=schemas.Project)
def update_project(
    id: int, project: schemas.ProjectUpdate, db: Session = Depends(get_db)
):
    return crud.update_project(db, id, project)


@router.delete("/{id}", response_model=schemas.Project)
def delete_project(id: int, db: Session = Depends(get_db)):
    return crud.delete_project(db, id)
