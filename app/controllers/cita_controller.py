from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.cita_model import CitaModel
from app.schema_validator.cita_validator import (
    CitaCreateValidator,
    CitaUpdateValidator,
)


class CitaController:
    @staticmethod
    def create(db: Session, data: CitaCreateValidator):
        return CitaModel.create(db=db, data=data.model_dump())

    @staticmethod
    def get_all(db: Session):
        return CitaModel.get_all(db=db)

    @staticmethod
    def get_by_id(db: Session, cita_id: int):
        cita = CitaModel.get_by_id(db=db, id_=cita_id)
        if cita is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Cita con id {cita_id} no encontrada",
            )
        return cita

    @staticmethod
    def update(db: Session, cita_id: int, data: CitaUpdateValidator):
        cita = CitaController.get_by_id(db=db, cita_id=cita_id)
        return CitaModel.update(db=db, obj=cita, data=data.model_dump())

    @staticmethod
    def delete(db: Session, cita_id: int):
        cita = CitaController.get_by_id(db=db, cita_id=cita_id)
        CitaModel.delete(db=db, obj=cita)
