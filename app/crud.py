from sqlalchemy.orm import Session
from . import models, schemas


def get_projects(db: Session):
    return db.query(models.Project).all()


def get_project(db: Session, project_id: int):
    return db.query(models.Project).filter(models.Project.id == project_id).first()


def create_project(db: Session, project: schemas.ProjectCreate):
    db_project = models.Project(**project.dict())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


def update_project(db: Session, project_id: int, project: schemas.ProjectUpdate):
    db_project = get_project(db, project_id)
    if db_project:
        for key, value in project.dict(exclude_unset=True).items():
            setattr(db_project, key, value)
        db.commit()
        db.refresh(db_project)
    return db_project


def delete_project(db: Session, project_id: int):
    db_project = get_project(db, project_id)
    if db_project:
        db.delete(db_project)
        db.commit()
    return db_project


def get_materials(db: Session):
    return db.query(models.Material).all()


def get_material(db: Session, material_id: int):
    return db.query(models.Material).filter(models.Material.id == material_id).first()


def create_material(db: Session, material: schemas.MaterialCreate):
    db_material = models.Material(**material.dict())
    db.add(db_material)
    db.commit()
    db.refresh(db_material)
    return db_material


def update_material(db: Session, material_id: int, material: schemas.MaterialUpdate):
    db_material = get_material(db, material_id)
    if db_material:
        for key, value in material.dict(exclude_unset=True).items():
            setattr(db_material, key, value)
        db.commit()
        db.refresh(db_material)
    return db_material


def delete_material(db: Session, material_id: int):
    db_material = get_material(db, material_id)
    if db_material:
        db.delete(db_material)
        db.commit()
    return db_material


def create_stock_entry(db: Session, entry: schemas.StockEntryCreate):
    db_entry = models.StockEntry(**entry.dict())
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry


def get_stock_entry(db: Session, entry_id: int):
    return db.query(models.StockEntry).filter(models.StockEntry.id == entry_id).first()


def update_stock_entry(
    db: Session, entry_id: int, entry: schemas.StockEntryUpdate
):
    db_entry = get_stock_entry(db, entry_id)
    if db_entry:
        for key, value in entry.dict(exclude_unset=True).items():
            setattr(db_entry, key, value)
        db.commit()
        db.refresh(db_entry)
    return db_entry


def delete_stock_entry(db: Session, entry_id: int):
    db_entry = get_stock_entry(db, entry_id)
    if db_entry:
        db.delete(db_entry)
        db.commit()
    return db_entry


def get_stock_by_project(db: Session, project_id: int):
    return db.query(models.StockEntry).filter(models.StockEntry.project_id == project_id).all()
