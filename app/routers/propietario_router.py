from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.controllers.propietario_controller import PropietarioController
from app.database.db_connection import get_db
from app.schema_validator.propietario_validator import (
    PropietarioCreateValidator,
    PropietarioUpdateValidator,
    PropietarioResponseValidator,
)

router = APIRouter(
    prefix="/propietarios",
    tags=["Propietarios"]
)
@router.post(
    "/",
    response_model=PropietarioResponseValidator,
    status_code=status.HTTP_201_CREATED,
)
def create_propietario(
        propietario_data: PropietarioCreateValidator,
        db: Session = Depends(get_db)):
    return PropietarioController.create(db=db, data=propietario_data)


@router.get(
    "/",
    response_model=list[PropietarioResponseValidator],
)
def get_propietarios(db: Session = Depends(get_db)):
    return PropietarioController.get_all(db=db)


@router.get(
    "/{propietario_id}",
    response_model=PropietarioResponseValidator,
)
def get_propietario(
        propietario_id: int,
        db: Session = Depends(get_db)):
    return PropietarioController.get_by_id(db=db, propietario_id=propietario_id)


@router.put(
    "/{propietario_id}",
    response_model=PropietarioResponseValidator,
)
def update_propietario(
        propietario_id: int,
        propietario_data: PropietarioUpdateValidator,
        db: Session = Depends(get_db)):
    return PropietarioController.update(db=db, propietario_id=propietario_id, data=propietario_data)


@router.delete(
    "/{propietario_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_propietario(
        propietario_id: int,
        db: Session = Depends(get_db)):
    PropietarioController.delete(db=db, propietario_id=propietario_id)
