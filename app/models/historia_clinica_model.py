from sqlalchemy.orm import Session
from app.schemas.historia_clinica_schema import HistoriaClinicaSchema


class HistoriaClinicaModel:
    @staticmethod
    def create(db: Session, mascota_id: int, peso: float, observaciones: str):
        historia = HistoriaClinicaSchema(
            mascota_id=mascota_id,
            peso=peso,
            observaciones=observaciones
        )
        db.add(historia)
        db.commit()
        db.refresh(historia)
        return historia
