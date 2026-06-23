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
