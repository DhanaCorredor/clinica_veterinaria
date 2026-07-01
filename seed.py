"""Vacia la base de datos y la recarga con los datos de datos_clinica.xlsx.

Uso:
    python seed.py

Lee cada pestaña del Excel (una por tabla), borra los datos actuales y vuelve a
insertar exactamente las filas del Excel, respetando el orden de las relaciones
(primero las tablas padre, luego las hijas) y conservando los id originales.
"""

from datetime import date, datetime

import openpyxl
from sqlalchemy import text

from app.database.db_connection import SessionLocal, engine, Base
from app.schemas.propietario_schema import PropietarioSchema
from app.schemas.veterinario_schema import VeterinarioSchema
from app.schemas.tratamiento_schema import TratamientoSchema
from app.schemas.mascota_schema import MascotaSchema
from app.schemas.historia_clinica_schema import HistoriaClinicaSchema
from app.schemas.cita_schema import CitaSchema
from app.schemas.mascota_tratamiento_schema import MascotaTratamientoSchema

EXCEL_FILE = "datos_clinica.xlsx"

# Orden de carga: primero padres, luego hijas (por las claves foraneas).
# Cada entrada: (nombre_de_hoja, modelo, {columna_excel: campo_modelo}, {campo: parser})
TABLAS = [
    ("propietarios", PropietarioSchema, {}, {}),
    ("veterinarios", VeterinarioSchema, {}, {}),
    ("tratamientos", TratamientoSchema, {}, {}),
    ("mascotas", MascotaSchema, {}, {"fecha_nacimiento": "date"}),
    ("historias_clinicas", HistoriaClinicaSchema, {"mascota_id (UNIQUE)": "mascota_id"}, {}),
    ("citas", CitaSchema, {}, {"fecha": "datetime"}),
    ("mascota_tratamiento", MascotaTratamientoSchema, {}, {"fecha_inicio": "date", "fecha_fin": "date"}),
]


def parsear(valor, tipo):
    """Convierte texto del Excel al tipo que espera la columna."""
    if valor is None or isinstance(valor, (date, datetime)):
        return valor
    if tipo == "date":
        return datetime.strptime(str(valor), "%Y-%m-%d").date()
    if tipo == "datetime":
        return datetime.strptime(str(valor), "%Y-%m-%d %H:%M")
    return valor


def leer_hoja(wb, hoja, renombres, parsers):
    """Devuelve la lista de dicts (una por fila) de una pestaña del Excel."""
    ws = wb[hoja]
    filas = list(ws.iter_rows(values_only=True))
    cabecera = [renombres.get(col, col) for col in filas[0]]
    registros = []
    for fila in filas[1:]:
        if all(celda is None for celda in fila):
            continue  # salta filas vacias
        datos = dict(zip(cabecera, fila))
        for campo, tipo in parsers.items():
            datos[campo] = parsear(datos[campo], tipo)
        registros.append(datos)
    return registros


def main():
    # Asegura que las tablas existan antes de tocarlas.
    Base.metadata.create_all(bind=engine)

    wb = openpyxl.load_workbook(EXCEL_FILE, data_only=True)
    db = SessionLocal()
    try:
        # 1. Vaciar: en orden inverso (hijas antes que padres) y reiniciar los id.
        nombres_tabla = [modelo.__tablename__ for _, modelo, _, _ in TABLAS]
        db.execute(
            text("TRUNCATE TABLE " + ", ".join(nombres_tabla) + " RESTART IDENTITY CASCADE")
        )
        db.commit()
        print("Tablas vaciadas.")

        # 2. Recargar: en orden (padres antes que hijas), conservando los id.
        for hoja, modelo, renombres, parsers in TABLAS:
            registros = leer_hoja(wb, hoja, renombres, parsers)
            db.bulk_insert_mappings(modelo, registros)
            db.commit()
            print(f"  {modelo.__tablename__}: {len(registros)} filas insertadas")

        # 3. Ajustar las secuencias de id para que los proximos inserts no choquen.
        for nombre in nombres_tabla:
            db.execute(
                text(
                    f"SELECT setval(pg_get_serial_sequence('{nombre}', 'id'), "
                    f"COALESCE((SELECT MAX(id) FROM {nombre}), 1))"
                )
            )
        db.commit()
        print("Secuencias de id ajustadas.")
        print("Sembrado completado.")
    finally:
        db.close()


if __name__ == "__main__":
    main()
