from app.models.base_model import BaseModel
from app.schemas.historia_clinica_schema import HistoriaClinicaSchema


class HistoriaClinicaModel(BaseModel):
    schema = HistoriaClinicaSchema
