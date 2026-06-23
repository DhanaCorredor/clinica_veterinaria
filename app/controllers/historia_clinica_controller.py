from sqlalchemy.orm import Session

from app.models.historia_clinica_model import HistoriaClinicaModel
from app.schema_validator.historia_clinica_validator import HistoriaClinicaCreateValidator


class HistoriaClinicaController:
    @staticmethod
    def create_historia_clinica(db: Session, historia_data: HistoriaClinicaCreateValidator):
        return HistoriaClinicaModel.create(
            db=db,
            mascota_id=historia_data.mascota_id,
            peso=historia_data.peso,
            observaciones=historia_data.observaciones
        )
