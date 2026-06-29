from app.models.base_model import BaseModel
from app.schemas.veterinario_schema import VeterinarioSchema


class VeterinarioModel(BaseModel):
    schema = VeterinarioSchema
