from app.models.base_model import BaseModel
from app.schemas.propietario_schema import PropietarioSchema


class PropietarioModel(BaseModel):
    schema = PropietarioSchema
