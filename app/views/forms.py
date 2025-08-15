
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

@router.post("/projects", response_class=HTMLResponse)
def create_project_html(
    request: Request,
    name: str = Form(...),
    location: str = Form(None),
    status: str = Form("active"),
    db: Session = Depends(get_db)
):
    project_data = schemas.ProjectCreate(name=name, location=location, status=status)
    crud.create_project(db, project_data)
    projects = crud.get_projects(db)
    return templates.TemplateResponse("partials/project_list.html", {"request": request, "projects": projects})

@router.get("/projects", response_class=HTMLResponse)
def view_projects(request: Request, db: Session = Depends(get_db)):
    projects = crud.get_projects(db)
    return templates.TemplateResponse("projects.html", {"request": request, "projects": projects})
