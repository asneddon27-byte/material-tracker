from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ProjectBase(BaseModel):
    name: str
    location: Optional[str] = None
    status: Optional[str] = "active"

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int
    class Config:
        orm_mode = True

class MaterialBase(BaseModel):
    name: str
    unit: str
    category: Optional[str] = None

class MaterialCreate(MaterialBase):
    pass

class Material(MaterialBase):
    id: int
    class Config:
        orm_mode = True

class StockEntryBase(BaseModel):
    project_id: int
    material_id: int
    quantity: float
    entry_type: str
    notes: Optional[str] = None

class StockEntryCreate(StockEntryBase):
    pass

class StockEntry(StockEntryBase):
    id: int
    date: datetime
    class Config:
        orm_mode = True
