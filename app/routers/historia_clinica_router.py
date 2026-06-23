from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.controllers.historia_clinica_controller import HistoriaClinicaController
from app.database.db_connection import get_db
from app.schema_validator.historia_clinica_validator import (
    HistoriaClinicaCreateValidator,
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
    return HistoriaClinicaController.create_historia_clinica(
        db=db,
        historia_data=historia_data)
