from datetime import date
from sqlalchemy.orm import Session
from app.schemas.mascota_tratamiento_schema import MascotaTratamientoSchema


class MascotaTratamientoModel:
    @staticmethod
    def create(db: Session, mascota_id: int, tratamiento_id: int,
               fecha_inicio: date, fecha_fin: date, dosis: str):
        registro = MascotaTratamientoSchema(
            mascota_id=mascota_id,
            tratamiento_id=tratamiento_id,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            dosis=dosis
        )
        db.add(registro)
        db.commit()
        db.refresh(registro)
        return registro
