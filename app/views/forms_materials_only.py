
from fastapi import APIRouter, Form, Request, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import crud, schemas
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/materials", response_class=HTMLResponse)
def create_material_html(
    request: Request,
    name: str = Form(...),
    unit: str = Form(...),
    category: str = Form(None),
    db: Session = Depends(get_db)
):
    material_data = schemas.MaterialCreate(name=name, unit=unit, category=category)
    crud.create_material(db, material_data)
    materials = crud.get_materials(db)
    return templates.TemplateResponse("partials/material_list.html", {"request": request, "materials": materials})

@router.get("/materials", response_class=HTMLResponse)
def view_materials(request: Request, db: Session = Depends(get_db)):
    materials = crud.get_materials(db)
    return templates.TemplateResponse("materials.html", {"request": request, "materials": materials})
