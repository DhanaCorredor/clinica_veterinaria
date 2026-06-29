from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.db_connection import get_db
from app.models.mascota_tratamiento_model import MascotaTratamientoModel
from app.schema_validator.mascota_tratamiento_validator import (
    MascotaTratamientoCreateValidator,
    MascotaTratamientoUpdateValidator,
    MascotaTratamientoResponseValidator,
)

router = APIRouter(
    prefix="/mascota_tratamiento",
    tags=["Mascota Tratamiento"]
)


def get_registro_or_404(db: Session, registro_id: int):
    registro = MascotaTratamientoModel.get_by_id(db=db, id_=registro_id)
    if registro is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Registro mascota-tratamiento con id {registro_id} no encontrado"
        )
    return registro


@router.post(
    "/",
    response_model=MascotaTratamientoResponseValidator,
    status_code=status.HTTP_201_CREATED,
)
def create_mascota_tratamiento(
        registro_data: MascotaTratamientoCreateValidator,
        db: Session = Depends(get_db)):
    return MascotaTratamientoModel.create(db=db, data=registro_data.model_dump())


@router.get(
    "/",
    response_model=list[MascotaTratamientoResponseValidator],
)
def get_registros(db: Session = Depends(get_db)):
    return MascotaTratamientoModel.get_all(db=db)


@router.get(
    "/{registro_id}",
    response_model=MascotaTratamientoResponseValidator,
)
def get_registro(
        registro_id: int,
        db: Session = Depends(get_db)):
    return get_registro_or_404(db=db, registro_id=registro_id)


@router.put(
    "/{registro_id}",
    response_model=MascotaTratamientoResponseValidator,
)
def update_registro(
        registro_id: int,
        registro_data: MascotaTratamientoUpdateValidator,
        db: Session = Depends(get_db)):
    registro = get_registro_or_404(db=db, registro_id=registro_id)
    return MascotaTratamientoModel.update(db=db, obj=registro, data=registro_data.model_dump())


@router.delete(
    "/{registro_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_registro(
        registro_id: int,
        db: Session = Depends(get_db)):
    registro = get_registro_or_404(db=db, registro_id=registro_id)
    MascotaTratamientoModel.delete(db=db, obj=registro)
