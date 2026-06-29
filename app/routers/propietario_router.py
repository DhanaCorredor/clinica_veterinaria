from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.db_connection import get_db
from app.models.propietario_model import PropietarioModel
from app.schema_validator.propietario_validator import (
    PropietarioCreateValidator,
    PropietarioUpdateValidator,
    PropietarioResponseValidator,
)

router = APIRouter(
    prefix="/propietarios",
    tags=["Propietarios"]
)


def get_propietario_or_404(db: Session, propietario_id: int):
    propietario = PropietarioModel.get_by_id(db=db, id_=propietario_id)
    if propietario is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Propietario con id {propietario_id} no encontrado"
        )
    return propietario


@router.post(
    "/",
    response_model=PropietarioResponseValidator,
    status_code=status.HTTP_201_CREATED,
)
def create_propietario(
        propietario_data: PropietarioCreateValidator,
        db: Session = Depends(get_db)):
    return PropietarioModel.create(db=db, data=propietario_data.model_dump())


@router.get(
    "/",
    response_model=list[PropietarioResponseValidator],
)
def get_propietarios(db: Session = Depends(get_db)):
    return PropietarioModel.get_all(db=db)


@router.get(
    "/{propietario_id}",
    response_model=PropietarioResponseValidator,
)
def get_propietario(
        propietario_id: int,
        db: Session = Depends(get_db)):
    return get_propietario_or_404(db=db, propietario_id=propietario_id)


@router.put(
    "/{propietario_id}",
    response_model=PropietarioResponseValidator,
)
def update_propietario(
        propietario_id: int,
        propietario_data: PropietarioUpdateValidator,
        db: Session = Depends(get_db)):
    propietario = get_propietario_or_404(db=db, propietario_id=propietario_id)
    return PropietarioModel.update(db=db, obj=propietario, data=propietario_data.model_dump())


@router.delete(
    "/{propietario_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_propietario(
        propietario_id: int,
        db: Session = Depends(get_db)):
    propietario = get_propietario_or_404(db=db, propietario_id=propietario_id)
    PropietarioModel.delete(db=db, obj=propietario)
