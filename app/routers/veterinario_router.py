from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.db_connection import get_db
from app.models.veterinario_model import VeterinarioModel
from app.schema_validator.veterinario_validator import (
    VeterinarioCreateValidator,
    VeterinarioUpdateValidator,
    VeterinarioResponseValidator,
)

router = APIRouter(
    prefix="/veterinarios",
    tags=["Veterinarios"]
)


def get_veterinario_or_404(db: Session, veterinario_id: int):
    veterinario = VeterinarioModel.get_by_id(db=db, veterinario_id=veterinario_id)
    if veterinario is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Veterinario con id {veterinario_id} no encontrado"
        )
    return veterinario


@router.post(
    "/",
    response_model=VeterinarioResponseValidator,
    status_code=status.HTTP_201_CREATED,
)
def create_veterinario(
        veterinario_data: VeterinarioCreateValidator,
        db: Session = Depends(get_db)):
    return VeterinarioModel.create(
        db=db,
        nombre=veterinario_data.nombre,
        especialidad=veterinario_data.especialidad
    )


@router.get(
    "/",
    response_model=list[VeterinarioResponseValidator],
)
def get_veterinarios(db: Session = Depends(get_db)):
    return VeterinarioModel.get_all(db=db)


@router.get(
    "/{veterinario_id}",
    response_model=VeterinarioResponseValidator,
)
def get_veterinario(
        veterinario_id: int,
        db: Session = Depends(get_db)):
    return get_veterinario_or_404(db=db, veterinario_id=veterinario_id)


@router.put(
    "/{veterinario_id}",
    response_model=VeterinarioResponseValidator,
)
def update_veterinario(
        veterinario_id: int,
        veterinario_data: VeterinarioUpdateValidator,
        db: Session = Depends(get_db)):
    veterinario = get_veterinario_or_404(db=db, veterinario_id=veterinario_id)
    return VeterinarioModel.update(
        db=db,
        veterinario=veterinario,
        nombre=veterinario_data.nombre,
        especialidad=veterinario_data.especialidad
    )


@router.delete(
    "/{veterinario_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_veterinario(
        veterinario_id: int,
        db: Session = Depends(get_db)):
    veterinario = get_veterinario_or_404(db=db, veterinario_id=veterinario_id)
    VeterinarioModel.delete(db=db, veterinario=veterinario)
