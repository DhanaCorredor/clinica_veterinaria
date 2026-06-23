from sqlalchemy.orm import Session

from app.models.propietario_model import PropietarioModel
from app.schema_validator.propietario_validator import PropietarioCreateValidator


class PropietarioController:
    @staticmethod
    def create_propietario(db: Session, propietario_data: PropietarioCreateValidator):
        return PropietarioModel.create(
            db=db,
            nombre=propietario_data.nombre,
            correo=propietario_data.correo,
            telefono=propietario_data.telefono
        )
