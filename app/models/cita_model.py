from app.models.base_model import BaseModel
from app.schemas.cita_schema import CitaSchema


class CitaModel(BaseModel):
    schema = CitaSchema
