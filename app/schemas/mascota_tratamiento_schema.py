from datetime import date
from sqlalchemy import String, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.database.db_connection import Base


class MascotaTratamientoSchema(Base):
    __tablename__ = "mascota_tratamiento"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    mascota_id: Mapped[int] = mapped_column(ForeignKey("mascotas.id"), nullable=False)
    tratamiento_id: Mapped[int] = mapped_column(ForeignKey("tratamientos.id"), nullable=False)
    fecha_inicio: Mapped[date] = mapped_column(Date, nullable=False)
    fecha_fin: Mapped[date] = mapped_column(Date, nullable=False)
    dosis: Mapped[str] = mapped_column(String(100), nullable=False)
