from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.controllers.veterinario_controller import VeterinarioController
from app.database.db_connection import get_db
from app.schema_validator.veterinario_validator import (
    VeterinarioCreateValidator,
    VeterinarioUpdateValidator,
    VeterinarioResponseValidator,
)

router = APIRouter(
    prefix="/veterinarios",
    tags=["Veterinarios"]
)


@router.post(
    "/",
    response_model=VeterinarioResponseValidator,
    status_code=status.HTTP_201_CREATED,
)
def create_veterinario(
        veterinario_data: VeterinarioCreateValidator,
        db: Session = Depends(get_db)):
    return VeterinarioController.create(db=db, data=veterinario_data)


@router.get(
    "/",
    response_model=list[VeterinarioResponseValidator],
)
def get_veterinarios(db: Session = Depends(get_db)):
    return VeterinarioController.get_all(db=db)


@router.get(
    "/{veterinario_id}",
    response_model=VeterinarioResponseValidator,
)
def get_veterinario(
        veterinario_id: int,
        db: Session = Depends(get_db)):
    return VeterinarioController.get_by_id(db=db, veterinario_id=veterinario_id)


@router.put(
    "/{veterinario_id}",
    response_model=VeterinarioResponseValidator,
)
def update_veterinario(
        veterinario_id: int,
        veterinario_data: VeterinarioUpdateValidator,
        db: Session = Depends(get_db)):
    return VeterinarioController.update(db=db, veterinario_id=veterinario_id, data=veterinario_data)


@router.delete(
    "/{veterinario_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_veterinario(
        veterinario_id: int,
        db: Session = Depends(get_db)):
    VeterinarioController.delete(db=db, veterinario_id=veterinario_id)
