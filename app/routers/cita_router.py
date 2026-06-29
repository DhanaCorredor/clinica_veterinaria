from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.db_connection import get_db
from app.models.cita_model import CitaModel
from app.schema_validator.cita_validator import (
    CitaCreateValidator,
    CitaUpdateValidator,
    CitaResponseValidator,
)

router = APIRouter(
    prefix="/citas",
    tags=["Citas"]
)


def get_cita_or_404(db: Session, cita_id: int):
    cita = CitaModel.get_by_id(db=db, id_=cita_id)
    if cita is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cita con id {cita_id} no encontrada"
        )
    return cita


@router.post(
    "/",
    response_model=CitaResponseValidator,
    status_code=status.HTTP_201_CREATED,
)
def create_cita(
        cita_data: CitaCreateValidator,
        db: Session = Depends(get_db)):
    return CitaModel.create(db=db, data=cita_data.model_dump())


@router.get(
    "/",
    response_model=list[CitaResponseValidator],
)
def get_citas(db: Session = Depends(get_db)):
    return CitaModel.get_all(db=db)


@router.get(
    "/{cita_id}",
    response_model=CitaResponseValidator,
)
def get_cita(
        cita_id: int,
        db: Session = Depends(get_db)):
    return get_cita_or_404(db=db, cita_id=cita_id)


@router.put(
    "/{cita_id}",
    response_model=CitaResponseValidator,
)
def update_cita(
        cita_id: int,
        cita_data: CitaUpdateValidator,
        db: Session = Depends(get_db)):
    cita = get_cita_or_404(db=db, cita_id=cita_id)
    return CitaModel.update(db=db, obj=cita, data=cita_data.model_dump())


@router.delete(
    "/{cita_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_cita(
        cita_id: int,
        db: Session = Depends(get_db)):
    cita = get_cita_or_404(db=db, cita_id=cita_id)
    CitaModel.delete(db=db, obj=cita)
