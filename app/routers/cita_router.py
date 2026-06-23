from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.controllers.cita_controller import CitaController
from app.database.db_connection import get_db
from app.schema_validator.cita_validator import (
    CitaCreateValidator,
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
    return CitaController.create_cita(
        db=db,
        cita_data=cita_data)
