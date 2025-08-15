from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ProjectBase(BaseModel):
    name: str
    location: Optional[str] = None
    status: Optional[str] = "active"

class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    location: Optional[str] = None
    status: Optional[str] = None

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


class MaterialUpdate(BaseModel):
    name: Optional[str] = None
    unit: Optional[str] = None
    category: Optional[str] = None

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


class StockEntryUpdate(BaseModel):
    project_id: Optional[int] = None
    material_id: Optional[int] = None
    quantity: Optional[float] = None
    entry_type: Optional[str] = None
    notes: Optional[str] = None

class StockEntry(StockEntryBase):
    id: int
    date: datetime
    class Config:
        orm_mode = True
