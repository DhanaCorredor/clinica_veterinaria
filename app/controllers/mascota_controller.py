from sqlalchemy.orm import Session

from app.models.mascota_model import MascotaModel
from app.schema_validator.mascota_validator import (
    MascotaCreateValidator,
    MascotaUpdateValidator,
)


class MascotaController:
    @staticmethod
    def create(db: Session, data: MascotaCreateValidator):
        return MascotaModel.create(db=db, data=data.model_dump())

    @staticmethod
    def get_all(db: Session):
        return MascotaModel.get_all(db=db)

    @staticmethod
    def get_by_id(db: Session, mascota_id: int):
        return MascotaModel.get_by_id(db=db, id_=mascota_id)

    @staticmethod
    def update(db: Session, mascota_id: int, data: MascotaUpdateValidator):
        mascota = MascotaController.get_by_id(db=db, mascota_id=mascota_id)
        return MascotaModel.update(db=db, obj=mascota, data=data.model_dump())

    @staticmethod
    def delete(db: Session, mascota_id: int):
        mascota = MascotaController.get_by_id(db=db, mascota_id=mascota_id)
        MascotaModel.delete(db=db, obj=mascota)
