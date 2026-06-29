from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.db_connection import get_db
from app.models.historia_clinica_model import HistoriaClinicaModel
from app.schema_validator.historia_clinica_validator import (
    HistoriaClinicaCreateValidator,
    HistoriaClinicaUpdateValidator,
    HistoriaClinicaResponseValidator,
)

router = APIRouter(
    prefix="/historias_clinicas",
    tags=["Historias Clinicas"]
)


def get_historia_or_404(db: Session, historia_id: int):
    historia = HistoriaClinicaModel.get_by_id(db=db, id_=historia_id)
    if historia is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Historia clinica con id {historia_id} no encontrada"
        )
    return historia


@router.post(
    "/",
    response_model=HistoriaClinicaResponseValidator,
    status_code=status.HTTP_201_CREATED,
)
def create_historia_clinica(
        historia_data: HistoriaClinicaCreateValidator,
        db: Session = Depends(get_db)):
    return HistoriaClinicaModel.create(db=db, data=historia_data.model_dump())


@router.get(
    "/",
    response_model=list[HistoriaClinicaResponseValidator],
)
def get_historias_clinicas(db: Session = Depends(get_db)):
    return HistoriaClinicaModel.get_all(db=db)


@router.get(
    "/{historia_id}",
    response_model=HistoriaClinicaResponseValidator,
)
def get_historia_clinica(
        historia_id: int,
        db: Session = Depends(get_db)):
    return get_historia_or_404(db=db, historia_id=historia_id)


@router.put(
    "/{historia_id}",
    response_model=HistoriaClinicaResponseValidator,
)
def update_historia_clinica(
        historia_id: int,
        historia_data: HistoriaClinicaUpdateValidator,
        db: Session = Depends(get_db)):
    historia = get_historia_or_404(db=db, historia_id=historia_id)
    return HistoriaClinicaModel.update(db=db, obj=historia, data=historia_data.model_dump())


@router.delete(
    "/{historia_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_historia_clinica(
        historia_id: int,
        db: Session = Depends(get_db)):
    historia = get_historia_or_404(db=db, historia_id=historia_id)
    HistoriaClinicaModel.delete(db=db, obj=historia)
