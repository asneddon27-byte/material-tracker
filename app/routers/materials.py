from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..database import SessionLocal

router = APIRouter(prefix="/materials", tags=["Materials"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.Material])
def list_materials(db: Session = Depends(get_db)):
    return crud.get_materials(db)

@router.post("/", response_model=schemas.Material)
def create_material(material: schemas.MaterialCreate, db: Session = Depends(get_db)):
    return crud.create_material(db, material)


@router.get("/{id}", response_model=schemas.Material)
def get_material(id: int, db: Session = Depends(get_db)):
    return crud.get_material(db, id)


@router.put("/{id}", response_model=schemas.Material)
def update_material(
    id: int, material: schemas.MaterialUpdate, db: Session = Depends(get_db)
):
    return crud.update_material(db, id, material)


@router.delete("/{id}", response_model=schemas.Material)
def delete_material(id: int, db: Session = Depends(get_db)):
    return crud.delete_material(db, id)
