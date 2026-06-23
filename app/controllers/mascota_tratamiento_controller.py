from sqlalchemy.orm import Session

from app.models.mascota_tratamiento_model import MascotaTratamientoModel
from app.schema_validator.mascota_tratamiento_validator import MascotaTratamientoCreateValidator


class MascotaTratamientoController:
    @staticmethod
    def create_mascota_tratamiento(db: Session, registro_data: MascotaTratamientoCreateValidator):
        return MascotaTratamientoModel.create(
            db=db,
            mascota_id=registro_data.mascota_id,
            tratamiento_id=registro_data.tratamiento_id,
            fecha_inicio=registro_data.fecha_inicio,
            fecha_fin=registro_data.fecha_fin,
            dosis=registro_data.dosis
        )
