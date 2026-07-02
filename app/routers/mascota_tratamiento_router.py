from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.controllers.mascota_tratamiento_controller import MascotaTratamientoController
from app.database.db_connection import get_db
from app.schema_validator.mascota_tratamiento_validator import (
    MascotaTratamientoCreateValidator,
    MascotaTratamientoUpdateValidator,
    MascotaTratamientoResponseValidator,
)

router = APIRouter(
    prefix="/mascota_tratamiento",
    tags=["Mascota Tratamiento"]
)


@router.post(
    "/",
    response_model=MascotaTratamientoResponseValidator,
    status_code=status.HTTP_201_CREATED,
)
def create_mascota_tratamiento(
        registro_data: MascotaTratamientoCreateValidator,
        db: Session = Depends(get_db)):
    return MascotaTratamientoController.create(db=db, data=registro_data)


@router.get(
    "/",
    response_model=list[MascotaTratamientoResponseValidator],
)
def get_registros(db: Session = Depends(get_db)):
    return MascotaTratamientoController.get_all(db=db)


@router.get(
    "/{registro_id}",
    response_model=MascotaTratamientoResponseValidator,
)
def get_registro(
        registro_id: int,
        db: Session = Depends(get_db)):
    return MascotaTratamientoController.get_by_id(db=db, registro_id=registro_id)


@router.put(
    "/{registro_id}",
    response_model=MascotaTratamientoResponseValidator,
)
def update_registro(
        registro_id: int,
        registro_data: MascotaTratamientoUpdateValidator,
        db: Session = Depends(get_db)):
    return MascotaTratamientoController.update(db=db, registro_id=registro_id, data=registro_data)


@router.delete(
    "/{registro_id}",
)
def delete_registro(
        registro_id: int,
        db: Session = Depends(get_db)):
    MascotaTratamientoController.delete(db=db, registro_id=registro_id)
