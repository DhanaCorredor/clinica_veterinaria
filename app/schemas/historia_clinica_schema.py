from sqlalchemy import String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.database.db_connection import Base


class HistoriaClinicaSchema(Base):
    __tablename__ = "historias_clinicas"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    mascota_id: Mapped[int] = mapped_column(ForeignKey("mascotas.id"), unique=True, nullable=False)
    peso: Mapped[float] = mapped_column(Float, nullable=False)
    observaciones: Mapped[str] = mapped_column(String(250), nullable=False)
