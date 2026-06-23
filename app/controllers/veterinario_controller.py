from sqlalchemy.orm import Session

from app.models.veterinario_model import VeterinarioModel
from app.schema_validator.veterinario_validator import VeterinarioCreateValidator


class VeterinarioController:
    @staticmethod
    def create_veterinario(db: Session, veterinario_data: VeterinarioCreateValidator):
        return VeterinarioModel.create(
            db=db,
            nombre=veterinario_data.nombre,
            especialidad=veterinario_data.especialidad
        )
