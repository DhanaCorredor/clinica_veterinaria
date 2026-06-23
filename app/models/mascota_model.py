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
