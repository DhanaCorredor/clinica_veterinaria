from pydantic import BaseModel


class TratamientoBaseValidator(BaseModel):
    nombre: str
    tipo: str
    costo: float


class TratamientoCreateValidator(TratamientoBaseValidator):
    pass


class TratamientoResponseValidator(TratamientoBaseValidator):
    id: int

    model_config = {
        "from_attributes": True
    }
