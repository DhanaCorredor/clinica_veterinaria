from sqlalchemy.orm import Session
from app.schemas.veterinario_schema import VeterinarioSchema


class VeterinarioModel:
    @staticmethod
    def create(db: Session, nombre: str, especialidad: str):
        veterinario = VeterinarioSchema(
            nombre=nombre,
            especialidad=especialidad
        )
        db.add(veterinario)
        db.commit()
        db.refresh(veterinario)
        return veterinario
