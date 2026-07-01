from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.veterinario_model import VeterinarioModel
from app.schema_validator.veterinario_validator import (
    VeterinarioCreateValidator,
    VeterinarioUpdateValidator,
)


class VeterinarioController:
    @staticmethod
    def create(db: Session, data: VeterinarioCreateValidator):
        return VeterinarioModel.create(db=db, data=data.model_dump())

    @staticmethod
    def get_all(db: Session):
        return VeterinarioModel.get_all(db=db)

    @staticmethod
    def get_by_id(db: Session, veterinario_id: int):
        veterinario = VeterinarioModel.get_by_id(db=db, id_=veterinario_id)
        if veterinario is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Veterinario con id {veterinario_id} no encontrado",
            )
        return veterinario

    @staticmethod
    def update(db: Session, veterinario_id: int, data: VeterinarioUpdateValidator):
        veterinario = VeterinarioController.get_by_id(db=db, veterinario_id=veterinario_id)
        return VeterinarioModel.update(db=db, obj=veterinario, data=data.model_dump())

    @staticmethod
    def delete(db: Session, veterinario_id: int):
        veterinario = VeterinarioController.get_by_id(db=db, veterinario_id=veterinario_id)
        VeterinarioModel.delete(db=db, obj=veterinario)
