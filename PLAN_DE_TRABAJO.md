# Plan de trabajo — API Clínica Veterinaria

API REST con **FastAPI + SQLAlchemy + PostgreSQL**. Arquitectura por capas:
`router → controller → model → schema (SQLAlchemy)` + validadores Pydantic.

## Estado actual

- ✅ Estructura del proyecto y arquitectura por capas montada.
- ✅ 7 entidades modeladas: propietario, veterinario, tratamiento, mascota, historia_clinica, cita, mascota_tratamiento.
- ✅ Conexión a BD, settings con `.env`, routers cableados en `main.py`, endpoint `/health-db`.
- ✅ Operación **CREATE (POST)** implementada en las 7 entidades.
- ⚠️ Solo existe el POST: falta el resto del CRUD.

## Qué falta (resumen)

| Área | Estado |
|------|--------|
| Crear (POST) | ✅ Hecho |
| Listar / Obtener / Actualizar / Eliminar | ❌ Falta |
| Manejo de errores (404 / 400) | ❌ Falta |
| Carga de datos desde `datos_clinica.xlsx` | ❌ Falta |
| Tests (pytest) | ❌ Falta |
| README / documentación | ❌ Falta |

---

## Fase 1 — Completar el CRUD (núcleo del proyecto)

Por cada una de las 7 entidades, añadir en las 3 capas (model → controller → router):

- [ ] `GET /` — listar todos
- [ ] `GET /{id}` — obtener por id (404 si no existe)
- [ ] `PUT /{id}` — actualizar (404 si no existe)
- [ ] `DELETE /{id}` — eliminar (404 si no existe)

**Subtareas por entidad:**
- [ ] propietario
- [ ] veterinario
- [ ] tratamiento
- [ ] mascota
- [ ] historia_clinica
- [ ] cita
- [ ] mascota_tratamiento

> Recomendación: hacer **mascota** completo primero como plantilla y replicar el patrón en el resto.

## Fase 2 — Manejo de errores

- [ ] Devolver `404 Not Found` (con `HTTPException`) cuando un id no existe.
- [ ] Validar claves foráneas (ej. crear mascota con `propietario_id` inexistente → `400/404`).
- [ ] Respuestas de error consistentes en toda la API.

## Fase 3 — Carga de datos desde Excel

- [ ] Añadir `openpyxl` (o `pandas`) a `requirements.txt`.
- [ ] Crear script de seed que lea `datos_clinica.xlsx` y puebla la BD respetando el orden de dependencias (propietarios → mascotas → historias/citas...).
- [ ] Documentar cómo ejecutarlo.

## Fase 4 — Tests

- [ ] Añadir `pytest` y `httpx` a `requirements.txt`.
- [ ] Crear carpeta `tests/` con `TestClient` de FastAPI.
- [ ] Test por entidad: crear, listar, obtener, actualizar, eliminar, y caso 404.

## Fase 5 — Documentación y cierre

- [ ] `README.md`: descripción, requisitos, instalación, configuración del `.env`, cómo arrancar (`uvicorn main:app --reload`), enlace a `/docs`.
- [ ] Revisar que `/docs` (Swagger) muestre todos los endpoints correctamente.
- [ ] Limpieza final y commit.

---

## Orden sugerido

1. **Fase 1** (CRUD) — es el grueso y lo que da valor a la API.
2. **Fase 2** (errores) — se puede ir haciendo junto con la Fase 1.
3. **Fase 3** (Excel) — para tener datos reales con los que probar.
4. **Fase 4** (tests).
5. **Fase 5** (README y cierre).
