from sqlalchemy.orm import Session
from . import models, schemas

def get_projects(db: Session):
    return db.query(models.Project).all()

def create_project(db: Session, project: schemas.ProjectCreate):
    db_project = models.Project(**project.dict())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

def get_materials(db: Session):
    return db.query(models.Material).all()

def create_material(db: Session, material: schemas.MaterialCreate):
    db_material = models.Material(**material.dict())
    db.add(db_material)
    db.commit()
    db.refresh(db_material)
    return db_material

def create_stock_entry(db: Session, entry: schemas.StockEntryCreate):
    db_entry = models.StockEntry(**entry.dict())
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry

def get_stock_by_project(db: Session, project_id: int):
    return db.query(models.StockEntry).filter(models.StockEntry.project_id == project_id).all()
