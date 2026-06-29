from pydantic import BaseModel


class PropietarioBaseValidator(BaseModel):
    nombre: str
    correo: str
    telefono: str


class PropietarioCreateValidator(PropietarioBaseValidator):
    pass


class PropietarioUpdateValidator(PropietarioBaseValidator):
    pass


class PropietarioResponseValidator(PropietarioBaseValidator):
    id: int

    model_config = {
        "from_attributes": True
    }
