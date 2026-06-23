from datetime import date
from pydantic import BaseModel


class MascotaBaseValidator(BaseModel):
    propietario_id: int
    nombre: str
    especie: str
    raza: str
    fecha_nacimiento: date


class MascotaCreateValidator(MascotaBaseValidator):
    pass


class MascotaResponseValidator(MascotaBaseValidator):
    id: int

    model_config = {
        "from_attributes": True
    }
