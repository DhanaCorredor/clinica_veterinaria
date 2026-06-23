from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.controllers.mascota_controller import MascotaController
from app.database.db_connection import get_db
from app.schema_validator.mascota_validator import (
    MascotaCreateValidator,
    MascotaResponseValidator,
)

router = APIRouter(
    prefix="/mascotas",
    tags=["Mascotas"]
)


@router.post(
    "/",
    response_model=MascotaResponseValidator,
    status_code=status.HTTP_201_CREATED,
)
def create_mascota(
        mascota_data: MascotaCreateValidator,
        db: Session = Depends(get_db)):
    return MascotaController.create_mascota(
        db=db,
        mascota_data=mascota_data)
