from datetime import date
from sqlalchemy import String, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.database.db_connection import Base


class MascotaSchema(Base):
    __tablename__ = "mascotas"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    propietario_id: Mapped[int] = mapped_column(ForeignKey("propietarios.id"), nullable=False)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    especie: Mapped[str] = mapped_column(String(50), nullable=False)
    raza: Mapped[str] = mapped_column(String(50), nullable=False)
    fecha_nacimiento: Mapped[date] = mapped_column(Date, nullable=False)
