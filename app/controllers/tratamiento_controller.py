from sqlalchemy.orm import Session

from app.models.tratamiento_model import TratamientoModel
from app.schema_validator.tratamiento_validator import (
    TratamientoCreateValidator,
    TratamientoUpdateValidator,
)


class TratamientoController:
    @staticmethod
    def create(db: Session, data: TratamientoCreateValidator):
        return TratamientoModel.create(db=db, data=data.model_dump())

    @staticmethod
    def get_all(db: Session):
        return TratamientoModel.get_all(db=db)

    @staticmethod
    def get_by_id(db: Session, tratamiento_id: int):
        return TratamientoModel.get_by_id(db=db, id_=tratamiento_id)

    @staticmethod
    def update(db: Session, tratamiento_id: int, data: TratamientoUpdateValidator):
        tratamiento = TratamientoController.get_by_id(db=db, tratamiento_id=tratamiento_id)
        return TratamientoModel.update(db=db, obj=tratamiento, data=data.model_dump())

    @staticmethod
    def delete(db: Session, tratamiento_id: int):
        tratamiento = TratamientoController.get_by_id(db=db, tratamiento_id=tratamiento_id)
        TratamientoModel.delete(db=db, obj=tratamiento)
