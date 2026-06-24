from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.mascota_model import MascotaModel
from app.schema_validator.mascota_validator import (
    MascotaCreateValidator,
    MascotaUpdateValidator,
)


class MascotaController:
    @staticmethod
    def create_mascota(db: Session, mascota_data: MascotaCreateValidator):
        return MascotaModel.create(
            db=db,
            propietario_id=mascota_data.propietario_id,
            nombre=mascota_data.nombre,
            especie=mascota_data.especie,
            raza=mascota_data.raza,
            fecha_nacimiento=mascota_data.fecha_nacimiento
        )

    @staticmethod
    def get_mascotas(db: Session):
        return MascotaModel.get_all(db=db)

    @staticmethod
    def get_mascota(db: Session, mascota_id: int):
        mascota = MascotaModel.get_by_id(db=db, mascota_id=mascota_id)
        if mascota is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Mascota con id {mascota_id} no encontrada"
            )
        return mascota

    @staticmethod
    def update_mascota(db: Session, mascota_id: int,
                       mascota_data: MascotaUpdateValidator):
        mascota = MascotaController.get_mascota(db=db, mascota_id=mascota_id)
        return MascotaModel.update(
            db=db,
            mascota=mascota,
            propietario_id=mascota_data.propietario_id,
            nombre=mascota_data.nombre,
            especie=mascota_data.especie,
            raza=mascota_data.raza,
            fecha_nacimiento=mascota_data.fecha_nacimiento
        )

    @staticmethod
    def delete_mascota(db: Session, mascota_id: int):
        mascota = MascotaController.get_mascota(db=db, mascota_id=mascota_id)
        MascotaModel.delete(db=db, mascota=mascota)
