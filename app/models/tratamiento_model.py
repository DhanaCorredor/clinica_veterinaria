from sqlalchemy.orm import Session
from app.schemas.tratamiento_schema import TratamientoSchema


class TratamientoModel:
    @staticmethod
    def create(db: Session, nombre: str, tipo: str, costo: float):
        tratamiento = TratamientoSchema(
            nombre=nombre,
            tipo=tipo,
            costo=costo
        )
        db.add(tratamiento)
        db.commit()
        db.refresh(tratamiento)
        return tratamiento
