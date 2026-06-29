from datetime import datetime
from sqlalchemy.orm import Session
from app.schemas.cita_schema import CitaSchema


class CitaModel:
    @staticmethod
    def create(db: Session, mascota_id: int, veterinario_id: int,
               fecha: datetime, estado: str):
        cita = CitaSchema(
            mascota_id=mascota_id,
            veterinario_id=veterinario_id,
            fecha=fecha,
            estado=estado
        )
        db.add(cita)
        db.commit()
        db.refresh(cita)
        return cita

    @staticmethod
    def get_all(db: Session):
        return db.query(CitaSchema).all()

    @staticmethod
    def get_by_id(db: Session, cita_id: int):
        return db.query(CitaSchema).filter(
            CitaSchema.id == cita_id
        ).first()

    @staticmethod
    def update(db: Session, cita: CitaSchema, mascota_id: int,
               veterinario_id: int, fecha: datetime, estado: str):
        cita.mascota_id = mascota_id
        cita.veterinario_id = veterinario_id
        cita.fecha = fecha
        cita.estado = estado
        db.commit()
        db.refresh(cita)
        return cita

    @staticmethod
    def delete(db: Session, cita: CitaSchema):
        db.delete(cita)
        db.commit()
