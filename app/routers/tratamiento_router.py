from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.db_connection import get_db
from app.models.tratamiento_model import TratamientoModel
from app.schema_validator.tratamiento_validator import (
    TratamientoCreateValidator,
    TratamientoUpdateValidator,
    TratamientoResponseValidator,
)

router = APIRouter(
    prefix="/tratamientos",
    tags=["Tratamientos"]
)


def get_tratamiento_or_404(db: Session, tratamiento_id: int):
    tratamiento = TratamientoModel.get_by_id(db=db, tratamiento_id=tratamiento_id)
    if tratamiento is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tratamiento con id {tratamiento_id} no encontrado"
        )
    return tratamiento


@router.post(
    "/",
    response_model=TratamientoResponseValidator,
    status_code=status.HTTP_201_CREATED,
)
def create_tratamiento(
        tratamiento_data: TratamientoCreateValidator,
        db: Session = Depends(get_db)):
    return TratamientoModel.create(
        db=db,
        nombre=tratamiento_data.nombre,
        tipo=tratamiento_data.tipo,
        costo=tratamiento_data.costo
    )


@router.get(
    "/",
    response_model=list[TratamientoResponseValidator],
)
def get_tratamientos(db: Session = Depends(get_db)):
    return TratamientoModel.get_all(db=db)


@router.get(
    "/{tratamiento_id}",
    response_model=TratamientoResponseValidator,
)
def get_tratamiento(
        tratamiento_id: int,
        db: Session = Depends(get_db)):
    return get_tratamiento_or_404(db=db, tratamiento_id=tratamiento_id)


@router.put(
    "/{tratamiento_id}",
    response_model=TratamientoResponseValidator,
)
def update_tratamiento(
        tratamiento_id: int,
        tratamiento_data: TratamientoUpdateValidator,
        db: Session = Depends(get_db)):
    tratamiento = get_tratamiento_or_404(db=db, tratamiento_id=tratamiento_id)
    return TratamientoModel.update(
        db=db,
        tratamiento=tratamiento,
        nombre=tratamiento_data.nombre,
        tipo=tratamiento_data.tipo,
        costo=tratamiento_data.costo
    )


@router.delete(
    "/{tratamiento_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_tratamiento(
        tratamiento_id: int,
        db: Session = Depends(get_db)):
    tratamiento = get_tratamiento_or_404(db=db, tratamiento_id=tratamiento_id)
    TratamientoModel.delete(db=db, tratamiento=tratamiento)
