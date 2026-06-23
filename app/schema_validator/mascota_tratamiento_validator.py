from datetime import date
from pydantic import BaseModel


class MascotaTratamientoBaseValidator(BaseModel):
    mascota_id: int
    tratamiento_id: int
    fecha_inicio: date
    fecha_fin: date
    dosis: str


class MascotaTratamientoCreateValidator(MascotaTratamientoBaseValidator):
    pass


class MascotaTratamientoResponseValidator(MascotaTratamientoBaseValidator):
    id: int

    model_config = {
        "from_attributes": True
    }
