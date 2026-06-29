from datetime import datetime
from pydantic import BaseModel


class CitaBaseValidator(BaseModel):
    mascota_id: int
    veterinario_id: int
    fecha: datetime
    estado: str


class CitaCreateValidator(CitaBaseValidator):
    pass


class CitaUpdateValidator(CitaBaseValidator):
    pass


class CitaResponseValidator(CitaBaseValidator):
    id: int

    model_config = {
        "from_attributes": True
    }
