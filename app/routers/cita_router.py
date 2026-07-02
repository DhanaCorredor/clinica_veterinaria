from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.controllers.cita_controller import CitaController
from app.database.db_connection import get_db
from app.schema_validator.cita_validator import (
    CitaCreateValidator,
    CitaUpdateValidator,
    CitaResponseValidator,
)

router = APIRouter(
    prefix="/citas",
    tags=["Citas"]
)


@router.post(
    "/",
    response_model=CitaResponseValidator,
    status_code=status.HTTP_201_CREATED,
)
def create_cita(
        cita_data: CitaCreateValidator,
        db: Session = Depends(get_db)):
    return CitaController.create(db=db, data=cita_data)


@router.get(
    "/",
    response_model=list[CitaResponseValidator],
)
def get_citas(db: Session = Depends(get_db)):
    return CitaController.get_all(db=db)


@router.get(
    "/{cita_id}",
    response_model=CitaResponseValidator,
)
def get_cita(
        cita_id: int,
        db: Session = Depends(get_db)):
    return CitaController.get_by_id(db=db, cita_id=cita_id)


@router.put(
    "/{cita_id}",
    response_model=CitaResponseValidator,
)
def update_cita(
        cita_id: int,
        cita_data: CitaUpdateValidator,
        db: Session = Depends(get_db)):
    return CitaController.update(db=db, cita_id=cita_id, data=cita_data)


@router.delete(
    "/{cita_id}",
)
def delete_cita(
        cita_id: int,
        db: Session = Depends(get_db)):
    CitaController.delete(db=db, cita_id=cita_id)
