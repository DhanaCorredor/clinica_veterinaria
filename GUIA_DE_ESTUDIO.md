# 🎓 Guía de estudio — API Clínica Veterinaria

Guía para presentar el proyecto. Léela de arriba abajo; las secciones 1–4 son el
"qué es y cómo funciona", la 5 son las **preguntas típicas con respuesta lista**.

---

## 1. Pitch de 30 segundos (cómo empezar la presentación)

> "Es una **API REST** para gestionar una clínica veterinaria: propietarios,
> mascotas, veterinarios, citas, tratamientos e historias clínicas. Está hecha
> en **Python con FastAPI**, usa **PostgreSQL** como base de datos y **SQLAlchemy**
> como ORM. Sigue una **arquitectura por capas** (router → controller → model →
> schema) con validación de datos mediante **Pydantic**. Tiene el **CRUD completo**
> de las 7 entidades con manejo de errores 404 y documentación automática con Swagger."

---

## 2. Stack tecnológico (y por qué cada pieza)

| Tecnología | Para qué sirve en tu proyecto |
|------------|-------------------------------|
| **FastAPI** | Framework web: define endpoints, valida, genera Swagger (`/docs`) |
| **Uvicorn** | Servidor ASGI que arranca la app (`uvicorn main:app --reload`) |
| **SQLAlchemy 2.0** | ORM: convierte clases Python ↔ tablas de la BD |
| **PostgreSQL** | La base de datos relacional |
| **psycopg** | El driver que conecta Python con PostgreSQL |
| **Pydantic v2** | Valida los datos de entrada/salida (los "validators") |
| **pydantic-settings** | Lee la configuración desde el archivo `.env` |

**Frase clave**: "FastAPI es asíncrono, rápido y genera documentación interactiva
sola. Elegí PostgreSQL por ser relacional, que encaja con datos con relaciones
como propietario→mascota→cita."

---

## 3. Arquitectura por capas (LO MÁS IMPORTANTE)

Cada petición HTTP atraviesa estas capas, **una responsabilidad por capa** (principio SRP):

```
Cliente HTTP
    │
    ▼
Router          →  app/routers/       define la ruta y el método HTTP
    │
    ▼
Validator       →  app/schema_validator/   valida entrada/salida (Pydantic)
    │
    ▼
Controller      →  app/controllers/    orquesta la operación + lanza el 404
    │
    ▼
Model           →  app/models/         habla con la BD (create, get, update, delete)
    │
    ▼
Schema (ORM)    →  app/schemas/        clase SQLAlchemy = tabla
    │
    ▼
PostgreSQL
```

**Por qué separar en capas**: cada archivo hace una sola cosa, es más fácil de
mantener, testear y entender. Si cambio la BD, solo toco los models; si cambio una
ruta, solo el router.

### Ejemplo real: `GET /mascotas/5`

1. **Router** (`mascota_router.py`) recibe la petición y llama al controller.
2. **Controller** (`mascota_controller.py`) pide la mascota al model; si no existe, lanza `404`.
3. **Model** (`mascota_model.py`) hereda de `BaseModel` y ejecuta la query.
4. **Schema** (`mascota_schema.py`) mapea la fila de la tabla a un objeto Python.
5. **Validator** (`mascota_validator.py`) serializa la respuesta a JSON limpio.

---

## 4. Conceptos que TIENES que saber defender

### 🔹 ORM (SQLAlchemy)
"Un ORM me deja trabajar con **objetos Python en vez de SQL a mano**. Mi clase
`MascotaSchema` es la tabla `mascotas`; cada atributo es una columna."
```python
class MascotaSchema(Base):
    __tablename__ = "mascotas"
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    propietario_id: Mapped[int] = mapped_column(ForeignKey("propietarios.id"))
```

### 🔹 Pydantic — los "validators"
"Definen **qué datos entran y salen** y los validan automáticamente. Si mando un
campo con el tipo equivocado, FastAPI responde `422` solo."
- `CreateValidator`: datos para crear (sin `id`).
- `UpdateValidator`: datos para actualizar.
- `ResponseValidator`: lo que devuelvo (con `id`, `from_attributes=True` para leer del objeto ORM).

### 🔹 Inyección de dependencias — `Depends(get_db)`
"`get_db` abre una sesión de BD por cada petición y la cierra al terminar
(`try/finally`). FastAPI me la inyecta automáticamente con `Depends`."

### 🔹 `response_model` y códigos HTTP
"Cada endpoint declara su `response_model`, así Swagger sabe la forma de la
respuesta. Uso `201` al crear, `204` al borrar, `404` si no existe el id."

### 🔹 BaseModel — herencia y DRY  ⭐ (punto fuerte para destacar)
"Como los 7 models repetían el mismo CRUD, extraje la lógica genérica
(`create/get_all/get_by_id/update/delete`) a un **`BaseModel`**. Cada model concreto
solo hereda y declara su tabla. Eso eliminó ~300 líneas duplicadas."
```python
class MascotaModel(BaseModel):
    schema = MascotaSchema
```

### 🔹 Manejo de errores (404)
"Si pido un id que no existe, el controller lanza `HTTPException(404)` con un
mensaje claro, en vez de devolver un error feo o `null`."

### 🔹 Configuración con `.env`
"Los datos sensibles (usuario/contraseña de la BD) están en un `.env` que **no se
sube a Git**. `settings.py` los lee con pydantic-settings y arma la URL de conexión."

---

## 5. Preguntas típicas del profe (CON RESPUESTA)

**P: ¿Por qué usaste FastAPI y no Django/Flask?**
R: Es rápido, asíncrono, valida solo con Pydantic y genera documentación
interactiva automáticamente. Ideal para APIs REST.

**P: ¿Qué es una API REST?**
R: Una interfaz que expone recursos (propietarios, mascotas...) a través de URLs
y métodos HTTP (GET leer, POST crear, PUT actualizar, DELETE borrar).

**P: ¿Qué hace el controller? ¿No es redundante con el router?**
R: El router solo define la ruta HTTP; el controller **orquesta la lógica** y
maneja errores como el 404. Separarlos mantiene el router limpio y deja un sitio
claro para la lógica de negocio (por ejemplo, validaciones futuras).

**P: ¿Cómo se relacionan las tablas?**
R: Un propietario tiene muchas mascotas (1:N); cada mascota tiene una historia
clínica (1:1); una mascota tiene muchas citas, cada cita con un veterinario;
mascotas y tratamientos es N:M mediante la tabla intermedia `mascota_tratamiento`.

**P: ¿Cómo se crean las tablas?**
R: Con `Base.metadata.create_all()` en el `lifespan` de `main.py`: al arrancar,
crea las tablas que falten.

**P: ¿Qué es Pydantic y qué diferencia hay con los schemas de SQLAlchemy?**
R: Los schemas de SQLAlchemy son las **tablas** (persistencia). Los validators de
Pydantic validan los **datos de la API** (entrada/salida). Son capas distintas.

**P: ¿Y Alembic / migraciones?** (por si lo pregunta al haberlo visto en clase)
R: Alembic versiona cambios del esquema sin perder datos. Para este proyecto uso
`create_all`, que es suficiente en desarrollo. Alembic sería el siguiente paso si
tuviera datos en producción o trabajara en equipo. *(Lo conozco, pero no era
necesario para el alcance actual.)*

**P: ¿Tiene tests?**
R: Todavía no; está en el plan de trabajo (`pytest` + `TestClient`). Verifiqué la
API manualmente con Swagger y probando el CRUD contra la BD.

**P: ¿Qué mejorarías / qué falta?**
R: 1) Validación de claves foráneas (crear una cita con un veterinario inexistente
debería dar error claro). 2) Tests automáticos. 3) Carga de datos desde el Excel.

---

## 6. Demo en vivo (guion para enseñarlo)

1. Arranca: `uvicorn main:app --reload`
2. Abre **http://localhost:8000/docs** (Swagger).
3. Enseña `GET /health-db` → confirma conexión a la BD.
4. Haz un **POST /propietarios** → crea uno.
5. **GET /propietarios** → aparece en la lista.
6. **GET /propietarios/{id}** con un id que no existe → enseña el **404**.
7. Enseña una **PUT** y una **DELETE**.
8. Cierra explicando la arquitectura por capas con un endpoint abierto en PyCharm.

> Consejo: ten la BD arrancada y con algún dato antes de presentar. Prueba el
> flujo completo una vez la noche antes.

---

## 7. Chuleta de un vistazo

- **Qué es**: API REST de clínica veterinaria (7 entidades, CRUD completo).
- **Stack**: FastAPI + SQLAlchemy + PostgreSQL + Pydantic.
- **Capas**: router → controller → model → schema (+ validators Pydantic).
- **Puntos fuertes**: arquitectura limpia por capas, `BaseModel` genérico (DRY),
  manejo de 404, documentación automática con Swagger.
- **Pendiente (sé honesta)**: validación de FKs, tests, seed desde Excel.
- **Comando estrella**: `uvicorn main:app --reload` → `/docs`.
```
