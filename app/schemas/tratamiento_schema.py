from sqlalchemy import String, Float
from sqlalchemy.orm import Mapped, mapped_column
from app.database.db_connection import Base


class TratamientoSchema(Base):
    __tablename__ = "tratamientos"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    tipo: Mapped[str] = mapped_column(String(100), nullable=False)
    costo: Mapped[float] = mapped_column(Float, nullable=False)
