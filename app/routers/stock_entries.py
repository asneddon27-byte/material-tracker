from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..database import SessionLocal

router = APIRouter(prefix="/stock", tags=["Stock Entries"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.StockEntry)
def add_stock_entry(entry: schemas.StockEntryCreate, db: Session = Depends(get_db)):
    return crud.create_stock_entry(db, entry)

@router.get("/project/{project_id}", response_model=list[schemas.StockEntry])
def get_project_stock(project_id: int, db: Session = Depends(get_db)):
    return crud.get_stock_by_project(db, project_id)


@router.get("/{id}", response_model=schemas.StockEntry)
def get_stock_entry(id: int, db: Session = Depends(get_db)):
    return crud.get_stock_entry(db, id)


@router.put("/{id}", response_model=schemas.StockEntry)
def update_stock_entry(
    id: int, entry: schemas.StockEntryUpdate, db: Session = Depends(get_db)
):
    return crud.update_stock_entry(db, id, entry)


@router.delete("/{id}", response_model=schemas.StockEntry)
def delete_stock_entry(id: int, db: Session = Depends(get_db)):
    return crud.delete_stock_entry(db, id)
