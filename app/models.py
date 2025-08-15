from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    location = Column(String)
    status = Column(String)

    stock_entries = relationship("StockEntry", back_populates="project")

class Material(Base):
    __tablename__ = "materials"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    unit = Column(String)
    category = Column(String)

    stock_entries = relationship("StockEntry", back_populates="material")

class StockEntry(Base):
    __tablename__ = "stock_entries"
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    material_id = Column(Integer, ForeignKey("materials.id"))
    quantity = Column(Float)
    entry_type = Column(String)
    date = Column(DateTime, default=datetime.utcnow)
    notes = Column(String)

    project = relationship("Project", back_populates="stock_entries")
    material = relationship("Material", back_populates="stock_entries")
