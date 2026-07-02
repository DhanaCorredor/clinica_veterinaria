from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.controllers.tratamiento_controller import TratamientoController
from app.database.db_connection import get_db
from app.schema_validator.tratamiento_validator import (
    TratamientoCreateValidator,
    TratamientoUpdateValidator,
    TratamientoResponseValidator,
)

router = APIRouter(
    prefix="/tratamientos",
    tags=["Tratamientos"]
)


@router.post(
    "/",
    response_model=TratamientoResponseValidator,
    status_code=status.HTTP_201_CREATED,
)
def create_tratamiento(
        tratamiento_data: TratamientoCreateValidator,
        db: Session = Depends(get_db)):
    return TratamientoController.create(db=db, data=tratamiento_data)


@router.get(
    "/",
    response_model=list[TratamientoResponseValidator],
)
def get_tratamientos(db: Session = Depends(get_db)):
    return TratamientoController.get_all(db=db)


@router.get(
    "/{tratamiento_id}",
    response_model=TratamientoResponseValidator,
)
def get_tratamiento(
        tratamiento_id: int,
        db: Session = Depends(get_db)):
    return TratamientoController.get_by_id(db=db, tratamiento_id=tratamiento_id)


@router.put(
    "/{tratamiento_id}",
    response_model=TratamientoResponseValidator,
)
def update_tratamiento(
        tratamiento_id: int,
        tratamiento_data: TratamientoUpdateValidator,
        db: Session = Depends(get_db)):
    return TratamientoController.update(db=db, tratamiento_id=tratamiento_id, data=tratamiento_data)


@router.delete(
    "/{tratamiento_id}",
)
def delete_tratamiento(
        tratamiento_id: int,
        db: Session = Depends(get_db)):
    TratamientoController.delete(db=db, tratamiento_id=tratamiento_id)
