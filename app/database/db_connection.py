from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from app.config.settings import settings

# Motor de conexion principal
engine = create_engine(settings.database_url, echo=settings.debug)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


class Base(DeclarativeBase):
    pass


def get_db():
    db = SessionLocal()
    try:
        yield db  # mantiene la sesion abierta durante la peticion
    finally:
        db.close()
