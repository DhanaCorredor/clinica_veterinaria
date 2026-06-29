from pydantic import BaseModel


class HistoriaClinicaBaseValidator(BaseModel):
    mascota_id: int
    peso: float
    observaciones: str


class HistoriaClinicaCreateValidator(HistoriaClinicaBaseValidator):
    pass


class HistoriaClinicaUpdateValidator(HistoriaClinicaBaseValidator):
    pass


class HistoriaClinicaResponseValidator(HistoriaClinicaBaseValidator):
    id: int

    model_config = {
        "from_attributes": True
    }
