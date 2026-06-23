from fastapi import FastAPI
from contextlib import asynccontextmanager
from sqlalchemy import text

from app.config.settings import settings
from app.database.db_connection import engine, Base
from app.routers.router_home import router as home_router
from app.routers.propietario_router import router as propietario_router
from app.routers.veterinario_router import router as veterinario_router
from app.routers.tratamiento_router import router as tratamiento_router
from app.routers.mascota_router import router as mascota_router
from app.routers.historia_clinica_router import router as historia_clinica_router
from app.routers.cita_router import router as cita_router
from app.schemas.propietario_schema import PropietarioSchema
from app.schemas.veterinario_schema import VeterinarioSchema
from app.schemas.tratamiento_schema import TratamientoSchema
from app.schemas.mascota_schema import MascotaSchema
from app.schemas.historia_clinica_schema import HistoriaClinicaSchema
from app.schemas.cita_schema import CitaSchema


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description=settings.app_description,
    lifespan=lifespan
)

app.include_router(home_router)
app.include_router(propietario_router)
app.include_router(veterinario_router)
app.include_router(tratamiento_router)
app.include_router(mascota_router)
app.include_router(historia_clinica_router)
app.include_router(cita_router)


@app.get("/health-db", tags=["health"])
def db_check():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    return {"message": "DB Health check successful"}
