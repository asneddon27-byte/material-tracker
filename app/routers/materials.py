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
