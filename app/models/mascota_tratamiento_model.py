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

    @staticmethod
    def get_all(db: Session):
        return db.query(MascotaTratamientoSchema).all()

    @staticmethod
    def get_by_id(db: Session, registro_id: int):
        return db.query(MascotaTratamientoSchema).filter(
            MascotaTratamientoSchema.id == registro_id
        ).first()

    @staticmethod
    def update(db: Session, registro: MascotaTratamientoSchema,
               mascota_id: int, tratamiento_id: int,
               fecha_inicio: date, fecha_fin: date, dosis: str):
        registro.mascota_id = mascota_id
        registro.tratamiento_id = tratamiento_id
        registro.fecha_inicio = fecha_inicio
        registro.fecha_fin = fecha_fin
        registro.dosis = dosis
        db.commit()
        db.refresh(registro)
        return registro

    @staticmethod
    def delete(db: Session, registro: MascotaTratamientoSchema):
        db.delete(registro)
        db.commit()
