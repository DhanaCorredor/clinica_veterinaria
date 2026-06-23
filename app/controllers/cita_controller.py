from sqlalchemy.orm import Session

from app.models.cita_model import CitaModel
from app.schema_validator.cita_validator import CitaCreateValidator


class CitaController:
    @staticmethod
    def create_cita(db: Session, cita_data: CitaCreateValidator):
        return CitaModel.create(
            db=db,
            mascota_id=cita_data.mascota_id,
            veterinario_id=cita_data.veterinario_id,
            fecha=cita_data.fecha,
            estado=cita_data.estado
        )
