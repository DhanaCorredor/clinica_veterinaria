from app.models.base_model import BaseModel
from app.schemas.mascota_schema import MascotaSchema


class MascotaModel(BaseModel):
    schema = MascotaSchema
