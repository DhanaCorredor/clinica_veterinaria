from datetime import datetime
from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.database.db_connection import Base


class CitaSchema(Base):
    __tablename__ = "citas"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    mascota_id: Mapped[int] = mapped_column(ForeignKey("mascotas.id"), nullable=False)
    veterinario_id: Mapped[int] = mapped_column(ForeignKey("veterinarios.id"), nullable=False)
    fecha: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    estado: Mapped[str] = mapped_column(String(50), nullable=False)
