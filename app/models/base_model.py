from typing import ClassVar

from sqlalchemy.orm import Session

from app.database.db_connection import Base


class BaseModel:
    """Operaciones CRUD genericas reutilizables por cada entidad.

    Cada model concreto solo declara `schema` con su clase SQLAlchemy;
    hereda create / get_all / get_by_id / update / delete de aqui.
    """

    schema: ClassVar[type[Base]]

    @classmethod
    def get_all(cls, db: Session):
        return db.query(cls.schema).all()

    @classmethod
    def get_by_id(cls, db: Session, id_: int):
        return db.query(cls.schema).filter(cls.schema.id == id_).first()

    @classmethod
    def create(cls, db: Session, data: dict):
        obj = cls.schema(**data)
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    @classmethod
    def update(cls, db: Session, obj, data: dict):
        for field, value in data.items():
            setattr(obj, field, value)
        db.commit()
        db.refresh(obj)
        return obj

    @classmethod
    def delete(cls, db: Session, obj) -> None:
        db.delete(obj)
        db.commit()
