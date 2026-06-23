from sqlalchemy.orm import Session

from app.models.tratamiento_model import TratamientoModel
from app.schema_validator.tratamiento_validator import TratamientoCreateValidator


class TratamientoController:
    @staticmethod
    def create_tratamiento(db: Session, tratamiento_data: TratamientoCreateValidator):
        return TratamientoModel.create(
            db=db,
            nombre=tratamiento_data.nombre,
            tipo=tratamiento_data.tipo,
            costo=tratamiento_data.costo
        )
