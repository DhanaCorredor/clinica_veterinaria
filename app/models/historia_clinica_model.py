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

    @staticmethod
    def get_all(db: Session):
        return db.query(HistoriaClinicaSchema).all()

    @staticmethod
    def get_by_id(db: Session, historia_id: int):
        return db.query(HistoriaClinicaSchema).filter(
            HistoriaClinicaSchema.id == historia_id
        ).first()

    @staticmethod
    def update(db: Session, historia: HistoriaClinicaSchema,
               mascota_id: int, peso: float, observaciones: str):
        historia.mascota_id = mascota_id
        historia.peso = peso
        historia.observaciones = observaciones
        db.commit()
        db.refresh(historia)
        return historia

    @staticmethod
    def delete(db: Session, historia: HistoriaClinicaSchema):
        db.delete(historia)
        db.commit()
