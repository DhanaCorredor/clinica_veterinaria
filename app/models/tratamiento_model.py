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

    @staticmethod
    def get_all(db: Session):
        return db.query(TratamientoSchema).all()

    @staticmethod
    def get_by_id(db: Session, tratamiento_id: int):
        return db.query(TratamientoSchema).filter(
            TratamientoSchema.id == tratamiento_id
        ).first()

    @staticmethod
    def update(db: Session, tratamiento: TratamientoSchema,
               nombre: str, tipo: str, costo: float):
        tratamiento.nombre = nombre
        tratamiento.tipo = tipo
        tratamiento.costo = costo
        db.commit()
        db.refresh(tratamiento)
        return tratamiento

    @staticmethod
    def delete(db: Session, tratamiento: TratamientoSchema):
        db.delete(tratamiento)
        db.commit()
