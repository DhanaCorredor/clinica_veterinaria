from datetime import date
from sqlalchemy.orm import Session
from app.schemas.mascota_schema import MascotaSchema


class MascotaModel:
    @staticmethod
    def create(db: Session, propietario_id: int, nombre: str,
               especie: str, raza: str, fecha_nacimiento: date):
        mascota = MascotaSchema(
            propietario_id=propietario_id,
            nombre=nombre,
            especie=especie,
            raza=raza,
            fecha_nacimiento=fecha_nacimiento
        )
        db.add(mascota)
        db.commit()
        db.refresh(mascota)
        return mascota

    @staticmethod
    def get_all(db: Session):
        return db.query(MascotaSchema).all()

    @staticmethod
    def get_by_id(db: Session, mascota_id: int):
        return db.query(MascotaSchema).filter(
            MascotaSchema.id == mascota_id
        ).first()

    @staticmethod
    def update(db: Session, mascota: MascotaSchema, propietario_id: int,
               nombre: str, especie: str, raza: str, fecha_nacimiento: date):
        mascota.propietario_id = propietario_id
        mascota.nombre = nombre
        mascota.especie = especie
        mascota.raza = raza
        mascota.fecha_nacimiento = fecha_nacimiento
        db.commit()
        db.refresh(mascota)
        return mascota

    @staticmethod
    def delete(db: Session, mascota: MascotaSchema):
        db.delete(mascota)
        db.commit()
