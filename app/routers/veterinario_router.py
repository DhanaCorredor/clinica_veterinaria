from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.controllers.veterinario_controller import VeterinarioController
from app.database.db_connection import get_db
from app.schema_validator.veterinario_validator import (
    VeterinarioCreateValidator,
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
    return VeterinarioController.create_veterinario(
        db=db,
        veterinario_data=veterinario_data)
