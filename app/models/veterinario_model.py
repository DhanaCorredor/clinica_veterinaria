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

    @staticmethod
    def get_all(db: Session):
        return db.query(VeterinarioSchema).all()

    @staticmethod
    def get_by_id(db: Session, veterinario_id: int):
        return db.query(VeterinarioSchema).filter(
            VeterinarioSchema.id == veterinario_id
        ).first()

    @staticmethod
    def update(db: Session, veterinario: VeterinarioSchema,
               nombre: str, especialidad: str):
        veterinario.nombre = nombre
        veterinario.especialidad = especialidad
        db.commit()
        db.refresh(veterinario)
        return veterinario

    @staticmethod
    def delete(db: Session, veterinario: VeterinarioSchema):
        db.delete(veterinario)
        db.commit()
