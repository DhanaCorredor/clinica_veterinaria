from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.controllers.tratamiento_controller import TratamientoController
from app.database.db_connection import get_db
from app.schema_validator.tratamiento_validator import (
    TratamientoCreateValidator,
    TratamientoResponseValidator,
)

router = APIRouter(
    prefix="/tratamientos",
    tags=["Tratamientos"]
)


@router.post(
    "/",
    response_model=TratamientoResponseValidator,
    status_code=status.HTTP_201_CREATED,
)
def create_tratamiento(
        tratamiento_data: TratamientoCreateValidator,
        db: Session = Depends(get_db)):
    return TratamientoController.create_tratamiento(
        db=db,
        tratamiento_data=tratamiento_data)
