from sqlalchemy.orm import Session
from app.schemas.propietario_schema import PropietarioSchema


class PropietarioModel:
    @staticmethod
    def create(db: Session, nombre: str, correo: str, telefono: str):
        propietario = PropietarioSchema(
            nombre=nombre,
            correo=correo,
            telefono=telefono
        )
        db.add(propietario)
        db.commit()
        db.refresh(propietario)
        return propietario

    @staticmethod
    def get_all(db: Session):
        return db.query(PropietarioSchema).all()

    @staticmethod
    def get_by_id(db: Session, propietario_id: int):
        return db.query(PropietarioSchema).filter(
            PropietarioSchema.id == propietario_id
        ).first()

    @staticmethod
    def update(db: Session, propietario: PropietarioSchema,
               nombre: str, correo: str, telefono: str):
        propietario.nombre = nombre
        propietario.correo = correo
        propietario.telefono = telefono
        db.commit()
        db.refresh(propietario)
        return propietario

    @staticmethod
    def delete(db: Session, propietario: PropietarioSchema):
        db.delete(propietario)
        db.commit()
