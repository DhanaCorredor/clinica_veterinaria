from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.controllers.mascota_controller import MascotaController
from app.database.db_connection import get_db
from app.schema_validator.mascota_validator import (
    MascotaCreateValidator,
    MascotaUpdateValidator,
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
    return MascotaController.create(db=db, data=mascota_data)


@router.get(
    "/",
    response_model=list[MascotaResponseValidator],
)
def get_mascotas(db: Session = Depends(get_db)):
    return MascotaController.get_all(db=db)


@router.get(
    "/{mascota_id}",
    response_model=MascotaResponseValidator,
)
def get_mascota(
        mascota_id: int,
        db: Session = Depends(get_db)):
    return MascotaController.get_by_id(db=db, mascota_id=mascota_id)


@router.put(
    "/{mascota_id}",
    response_model=MascotaResponseValidator,
)
def update_mascota(
        mascota_id: int,
        mascota_data: MascotaUpdateValidator,
        db: Session = Depends(get_db)):
    return MascotaController.update(db=db, mascota_id=mascota_id, data=mascota_data)


@router.delete(
    "/{mascota_id}",
)
def delete_mascota(
        mascota_id: int,
        db: Session = Depends(get_db)):
    MascotaController.delete(db=db, mascota_id=mascota_id)
