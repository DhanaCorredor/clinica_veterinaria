from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.controllers.historia_clinica_controller import HistoriaClinicaController
from app.database.db_connection import get_db
from app.schema_validator.historia_clinica_validator import (
    HistoriaClinicaCreateValidator,
    HistoriaClinicaUpdateValidator,
    HistoriaClinicaResponseValidator,
)

router = APIRouter(
    prefix="/historias_clinicas",
    tags=["Historias Clinicas"]
)


@router.post(
    "/",
    response_model=HistoriaClinicaResponseValidator,
    status_code=status.HTTP_201_CREATED,
)
def create_historia_clinica(
        historia_data: HistoriaClinicaCreateValidator,
        db: Session = Depends(get_db)):
    return HistoriaClinicaController.create(db=db, data=historia_data)


@router.get(
    "/",
    response_model=list[HistoriaClinicaResponseValidator],
)
def get_historias_clinicas(db: Session = Depends(get_db)):
    return HistoriaClinicaController.get_all(db=db)


@router.get(
    "/{historia_id}",
    response_model=HistoriaClinicaResponseValidator,
)
def get_historia_clinica(
        historia_id: int,
        db: Session = Depends(get_db)):
    return HistoriaClinicaController.get_by_id(db=db, historia_id=historia_id)


@router.put(
    "/{historia_id}",
    response_model=HistoriaClinicaResponseValidator,
)
def update_historia_clinica(
        historia_id: int,
        historia_data: HistoriaClinicaUpdateValidator,
        db: Session = Depends(get_db)):
    return HistoriaClinicaController.update(db=db, historia_id=historia_id, data=historia_data)


@router.delete(
    "/{historia_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_historia_clinica(
        historia_id: int,
        db: Session = Depends(get_db)):
    HistoriaClinicaController.delete(db=db, historia_id=historia_id)
