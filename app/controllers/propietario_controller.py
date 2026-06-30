from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.propietario_model import PropietarioModel
from app.schema_validator.propietario_validator import (
    PropietarioCreateValidator,
    PropietarioUpdateValidator,
)


class PropietarioController:
    @staticmethod
    def create(db: Session, data: PropietarioCreateValidator):
        return PropietarioModel.create(db=db, data=data.model_dump())

    @staticmethod
    def get_all(db: Session):
        return PropietarioModel.get_all(db=db)

    @staticmethod
    def get_by_id(db: Session, propietario_id: int):
        propietario = PropietarioModel.get_by_id(db=db, id_=propietario_id)
        if propietario is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Propietario con id {propietario_id} no encontrado",
            )
        return propietario

    @staticmethod
    def update(db: Session, propietario_id: int, data: PropietarioUpdateValidator):
        propietario = PropietarioController.get_by_id(db=db, propietario_id=propietario_id)
        return PropietarioModel.update(db=db, obj=propietario, data=data.model_dump())

    @staticmethod
    def delete(db: Session, propietario_id: int):
        propietario = PropietarioController.get_by_id(db=db, propietario_id=propietario_id)
        PropietarioModel.delete(db=db, obj=propietario)
