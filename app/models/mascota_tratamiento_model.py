from app.models.base_model import BaseModel
from app.schemas.mascota_tratamiento_schema import MascotaTratamientoSchema


class MascotaTratamientoModel(BaseModel):
    schema = MascotaTratamientoSchema
