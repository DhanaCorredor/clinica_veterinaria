from sqlalchemy.orm import Session

from app.models.mascota_model import MascotaModel
from app.schema_validator.mascota_validator import MascotaCreateValidator


class MascotaController:
    @staticmethod
    def create_mascota(db: Session, mascota_data: MascotaCreateValidator):
        return MascotaModel.create(
            db=db,
            propietario_id=mascota_data.propietario_id,
            nombre=mascota_data.nombre,
            especie=mascota_data.especie,
            raza=mascota_data.raza,
            fecha_nacimiento=mascota_data.fecha_nacimiento
        )
