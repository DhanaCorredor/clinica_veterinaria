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
