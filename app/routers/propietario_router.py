from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.controllers.propietario_controller import PropietarioController
from app.database.db_connection import get_db
from app.schema_validator.propietario_validator import (
    PropietarioCreateValidator,
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
    return PropietarioController.create_propietario(
        db=db,
        propietario_data=propietario_data)
