from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.database.db_connection import Base


class VeterinarioSchema(Base):
    __tablename__ = "veterinarios"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    especialidad: Mapped[str] = mapped_column(String(100), nullable=False)
