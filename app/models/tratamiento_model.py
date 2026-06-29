from app.models.base_model import BaseModel
from app.schemas.tratamiento_schema import TratamientoSchema


class TratamientoModel(BaseModel):
    schema = TratamientoSchema
