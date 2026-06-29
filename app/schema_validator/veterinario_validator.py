from pydantic import BaseModel


class VeterinarioBaseValidator(BaseModel):
    nombre: str
    especialidad: str


class VeterinarioCreateValidator(VeterinarioBaseValidator):
    pass


class VeterinarioUpdateValidator(VeterinarioBaseValidator):
    pass


class VeterinarioResponseValidator(VeterinarioBaseValidator):
    id: int

    model_config = {
        "from_attributes": True
    }
