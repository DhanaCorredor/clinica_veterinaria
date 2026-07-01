# Plan de trabajo — API Clínica Veterinaria

API REST con **FastAPI + SQLAlchemy + PostgreSQL**. Arquitectura por capas:
`router → controller → model → schema (SQLAlchemy)` + validadores Pydantic. El CRUD genérico vive en `BaseModel`.

## Estado actual

- ✅ Estructura del proyecto y arquitectura por capas montada.
- ✅ 7 entidades modeladas: propietario, veterinario, tratamiento, mascota, historia_clinica, cita, mascota_tratamiento.
- ✅ Conexión a BD, settings con `.env`, routers cableados en `main.py`, endpoint `/health-db`.
- ✅ **CRUD completo (POST, GET, GET/{id}, PUT, DELETE) en las 7 entidades**, con manejo de 404.

## Qué falta (resumen)

| Área | Estado |
|------|--------|
| CRUD completo (7 entidades) | ✅ Hecho |
| Manejo de 404 | ✅ Hecho |
| Validación de claves foráneas (400) | ❌ Falta |
| Carga de datos desde `datos_clinica.xlsx` | ✅ Hecho (`seed.py`) |
| Tests (pytest) | ❌ Falta |
| README / documentación | ✅ Hecho (revisar al cierre) |

---

## Fase 1 — Completar el CRUD (núcleo del proyecto)

Por cada una de las 7 entidades, añadir en las 2 capas (model → router):

- [x] `GET /` — listar todos
- [x] `GET /{id}` — obtener por id (404 si no existe)
- [x] `PUT /{id}` — actualizar (404 si no existe)
- [x] `DELETE /{id}` — eliminar (404 si no existe)

**Subtareas por entidad:**
- [x] propietario
- [x] veterinario
- [x] tratamiento
- [x] mascota
- [x] historia_clinica
- [x] cita
- [x] mascota_tratamiento

> ✅ Fase 1 completada: las 7 entidades tienen el CRUD completo con manejo de 404.

## Fase 2 — Manejo de errores

- [x] Devolver `404 Not Found` (con `HTTPException`) cuando un id no existe — hecho en las 7 entidades (helper `get_X_or_404`).
- [ ] Validar claves foráneas (ej. crear mascota con `propietario_id` inexistente → `400/404`).
- [ ] Respuestas de error consistentes en toda la API.

## Fase 3 — Carga de datos desde Excel

- [x] Añadir `openpyxl` a `requirements.txt`.
- [x] Crear script de seed que lea `datos_clinica.xlsx` y puebla la BD respetando el orden de dependencias (propietarios → mascotas → historias/citas...).
- [x] Documentar cómo ejecutarlo.

> ✅ Fase 3 completada: `seed.py` vacía y recarga las 7 tablas con los datos del Excel (padres antes que hijas, conservando los id). Ejecutar con `python seed.py`.

## Fase 4 — Tests

- [ ] Añadir `pytest` y `httpx` a `requirements.txt`.
- [ ] Crear carpeta `tests/` con `TestClient` de FastAPI.
- [ ] Test por entidad: crear, listar, obtener, actualizar, eliminar, y caso 404.

## Fase 5 — Documentación y cierre

- [x] `README.md`: descripción, requisitos, instalación, configuración del `.env`, cómo arrancar (`uvicorn main:app --reload`), enlace a `/docs`.
- [x] Revisar que `/docs` (Swagger) muestre todos los endpoints correctamente — verificado vía esquema OpenAPI (37 endpoints).
- [ ] Limpieza final y commit.

---

## Orden sugerido

1. ~~**Fase 1** (CRUD) — es el grueso y lo que da valor a la API.~~ ✅
2. **Fase 2** (errores) — validación de claves foráneas (400) pendiente.
3. ~~**Fase 3** (Excel) — para tener datos reales con los que probar.~~ ✅
4. **Fase 4** (tests).
5. **Fase 5** (README y cierre).
