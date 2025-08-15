from fastapi import FastAPI
from .routers import projects, materials, stock_entries
from .database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Material Tracker")

app.include_router(projects.router)
app.include_router(materials.router)
app.include_router(stock_entries.router)

@app.get("/")
def read_root():
    return {"msg": "Welcome to the Construction Material Tracker API"}
