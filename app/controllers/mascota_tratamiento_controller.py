from sqlalchemy.orm import Session

from app.models.mascota_tratamiento_model import MascotaTratamientoModel
from app.schema_validator.mascota_tratamiento_validator import (
    MascotaTratamientoCreateValidator,
    MascotaTratamientoUpdateValidator,
)


class MascotaTratamientoController:
    @staticmethod
    def create(db: Session, data: MascotaTratamientoCreateValidator):
        return MascotaTratamientoModel.create(db=db, data=data.model_dump())

    @staticmethod
    def get_all(db: Session):
        return MascotaTratamientoModel.get_all(db=db)

    @staticmethod
    def get_by_id(db: Session, registro_id: int):
        return MascotaTratamientoModel.get_by_id(db=db, id_=registro_id)

    @staticmethod
    def update(db: Session, registro_id: int, data: MascotaTratamientoUpdateValidator):
        registro = MascotaTratamientoController.get_by_id(db=db, registro_id=registro_id)
        return MascotaTratamientoModel.update(db=db, obj=registro, data=data.model_dump())

    @staticmethod
    def delete(db: Session, registro_id: int):
        registro = MascotaTratamientoController.get_by_id(db=db, registro_id=registro_id)
        MascotaTratamientoModel.delete(db=db, obj=registro)
