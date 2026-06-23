from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.controllers.mascota_tratamiento_controller import MascotaTratamientoController
from app.database.db_connection import get_db
from app.schema_validator.mascota_tratamiento_validator import (
    MascotaTratamientoCreateValidator,
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
    return MascotaTratamientoController.create_mascota_tratamiento(
        db=db,
        registro_data=registro_data)
