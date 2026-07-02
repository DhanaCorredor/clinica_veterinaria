from sqlalchemy.orm import Session

from app.models.historia_clinica_model import HistoriaClinicaModel
from app.schema_validator.historia_clinica_validator import (
    HistoriaClinicaCreateValidator,
    HistoriaClinicaUpdateValidator,
)


class HistoriaClinicaController:
    @staticmethod
    def create(db: Session, data: HistoriaClinicaCreateValidator):
        return HistoriaClinicaModel.create(db=db, data=data.model_dump())

    @staticmethod
    def get_all(db: Session):
        return HistoriaClinicaModel.get_all(db=db)

    @staticmethod
    def get_by_id(db: Session, historia_id: int):
        return HistoriaClinicaModel.get_by_id(db=db, id_=historia_id)

    @staticmethod
    def update(db: Session, historia_id: int, data: HistoriaClinicaUpdateValidator):
        historia = HistoriaClinicaController.get_by_id(db=db, historia_id=historia_id)
        return HistoriaClinicaModel.update(db=db, obj=historia, data=data.model_dump())

    @staticmethod
    def delete(db: Session, historia_id: int):
        historia = HistoriaClinicaController.get_by_id(db=db, historia_id=historia_id)
        HistoriaClinicaModel.delete(db=db, obj=historia)
