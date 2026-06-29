from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.db_connection import get_db
from app.models.mascota_model import MascotaModel
from app.schema_validator.mascota_validator import (
    MascotaCreateValidator,
    MascotaUpdateValidator,
    MascotaResponseValidator,
)

router = APIRouter(
    prefix="/mascotas",
    tags=["Mascotas"]
)


def get_mascota_or_404(db: Session, mascota_id: int):
    mascota = MascotaModel.get_by_id(db=db, id_=mascota_id)
    if mascota is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Mascota con id {mascota_id} no encontrada"
        )
    return mascota


@router.post(
    "/",
    response_model=MascotaResponseValidator,
    status_code=status.HTTP_201_CREATED,
)
def create_mascota(
        mascota_data: MascotaCreateValidator,
        db: Session = Depends(get_db)):
    return MascotaModel.create(db=db, data=mascota_data.model_dump())


@router.get(
    "/",
    response_model=list[MascotaResponseValidator],
)
def get_mascotas(db: Session = Depends(get_db)):
    return MascotaModel.get_all(db=db)


@router.get(
    "/{mascota_id}",
    response_model=MascotaResponseValidator,
)
def get_mascota(
        mascota_id: int,
        db: Session = Depends(get_db)):
    return get_mascota_or_404(db=db, mascota_id=mascota_id)


@router.put(
    "/{mascota_id}",
    response_model=MascotaResponseValidator,
)
def update_mascota(
        mascota_id: int,
        mascota_data: MascotaUpdateValidator,
        db: Session = Depends(get_db)):
    mascota = get_mascota_or_404(db=db, mascota_id=mascota_id)
    return MascotaModel.update(db=db, obj=mascota, data=mascota_data.model_dump())


@router.delete(
    "/{mascota_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_mascota(
        mascota_id: int,
        db: Session = Depends(get_db)):
    mascota = get_mascota_or_404(db=db, mascota_id=mascota_id)
    MascotaModel.delete(db=db, obj=mascota)
