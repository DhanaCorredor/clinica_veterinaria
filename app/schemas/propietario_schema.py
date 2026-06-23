from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.database.db_connection import Base


class PropietarioSchema(Base):
    __tablename__ = "propietarios"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    correo: Mapped[str] = mapped_column(String(150), nullable=False)
    telefono: Mapped[str] = mapped_column(String(20), nullable=False)
