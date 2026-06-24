# 🐾 API Clínica Veterinaria

> API REST para la gestión de una clínica veterinaria: propietarios, mascotas, veterinarios, citas, tratamientos e historias clínicas.
> Proyecto **Factoría F5**.

📖 **Wiki completa en Notion:** [API Clínica Veterinaria](https://dhanacorredor.notion.site/API-Cl-nica-Veterinaria-38954980d234801b8a4ffd25266a69fd)

---

## 1. Descripción general

Esta API permite gestionar la operativa de una clínica veterinaria. Centraliza la información de los **propietarios** y sus **mascotas**, el personal (**veterinarios**), los **tratamientos** ofrecidos, las **citas** agendadas, la **historia clínica** de cada mascota y la relación entre mascotas y los tratamientos aplicados.

Está construida como una **API REST** con documentación interactiva automática (Swagger / OpenAPI).

---

## 2. Stack tecnológico

| Componente | Tecnología |
|------------|------------|
| Lenguaje | Python 3.10+ |
| Framework web | FastAPI |
| Servidor ASGI | Uvicorn |
| ORM | SQLAlchemy 2.0 (estilo `Mapped` / `mapped_column`) |
| Base de datos | PostgreSQL |
| Driver BD | psycopg (binary) |
| Validación | Pydantic + pydantic-settings |
| Configuración | Variables de entorno vía `.env` |

---

## 3. Arquitectura

El proyecto sigue una **arquitectura por capas** con responsabilidad única por clase. El flujo de una petición es:

```
Cliente HTTP
    │
    ▼
Router          → define la ruta y el método HTTP (endpoint)
    │
    ▼
Validator       → valida/serializa datos de entrada y salida (Pydantic)
    │
    ▼
Controller      → orquesta la lógica de la operación
    │
    ▼
Model           → ejecuta la operación sobre la BD
    │
    ▼
Schema          → mapeo objeto-tabla (SQLAlchemy ORM)
    │
    ▼
PostgreSQL
```

### Significado de cada capa

- **Router** (`app/routers/`): expone los endpoints HTTP y delega en el controller. No contiene lógica de negocio.
- **Validator** (`app/schema_validator/`): modelos Pydantic que definen qué datos entran (`Create`) y qué datos salen (`Response`).
- **Controller** (`app/controllers/`): coordina la operación; recibe los datos validados y llama al model.
- **Model** (`app/models/`): contiene los métodos que hablan con la base de datos (`create`, etc.).
- **Schema** (`app/schemas/`): clases SQLAlchemy que representan las tablas.

---

## 4. Estructura de carpetas

```
clinica_veterinaria/
├── app/
│   ├── config/
│   │   └── settings.py              # Configuración (lee .env)
│   ├── controllers/                 # Lógica de cada entidad
│   ├── database/
│   │   └── db_connection.py         # Engine, sesión y Base
│   ├── models/                      # Operaciones contra la BD
│   ├── routers/                     # Endpoints HTTP
│   ├── schema_validator/            # Validadores Pydantic (entrada/salida)
│   └── schemas/                     # Tablas SQLAlchemy (ORM)
├── datos_clinica.xlsx               # Datos de ejemplo para poblar la BD
├── Diagrama-veterinaria.drawio      # Diagrama entidad-relación
├── main.py                          # Punto de entrada (crea la app y cablea routers)
├── requirements.txt
├── .env.example                     # Plantilla de variables de entorno
└── PLAN_DE_TRABAJO.md
```

---

## 5. Modelo de datos

La API gestiona **7 entidades**.

### Propietario
Dueño de una o varias mascotas.

| Campo | Tipo | Restricciones |
|-------|------|---------------|
| id | int | PK |
| nombre | str(100) | obligatorio |
| correo | str(150) | obligatorio |
| telefono | str(20) | obligatorio |

### Veterinario
Profesional que atiende las citas.

| Campo | Tipo | Restricciones |
|-------|------|---------------|
| id | int | PK |
| nombre | str(100) | obligatorio |
| especialidad | str(100) | obligatorio |

### Tratamiento
Servicio o tratamiento que ofrece la clínica.

| Campo | Tipo | Restricciones |
|-------|------|---------------|
| id | int | PK |
| nombre | str(100) | obligatorio |
| tipo | str(100) | obligatorio |
| costo | float | obligatorio |

### Mascota
Animal asociado a un propietario.

| Campo | Tipo | Restricciones |
|-------|------|---------------|
| id | int | PK |
| propietario_id | int | FK → propietarios.id, obligatorio |
| nombre | str(100) | obligatorio |
| especie | str(50) | obligatorio |
| raza | str(50) | obligatorio |
| fecha_nacimiento | date | obligatorio |

### Historia Clínica
Ficha clínica única de cada mascota (relación 1:1).

| Campo | Tipo | Restricciones |
|-------|------|---------------|
| id | int | PK |
| mascota_id | int | FK → mascotas.id, **único**, obligatorio |
| peso | float | obligatorio |
| observaciones | str(250) | obligatorio |

### Cita
Agenda de una visita de una mascota con un veterinario.

| Campo | Tipo | Restricciones |
|-------|------|---------------|
| id | int | PK |
| mascota_id | int | FK → mascotas.id, obligatorio |
| veterinario_id | int | FK → veterinarios.id, obligatorio |
| fecha | datetime | obligatorio |
| estado | str(50) | obligatorio |

### Mascota–Tratamiento
Tabla intermedia (N:M) que registra los tratamientos aplicados a una mascota.

| Campo | Tipo | Restricciones |
|-------|------|---------------|
| id | int | PK |
| mascota_id | int | FK → mascotas.id, obligatorio |
| tratamiento_id | int | FK → tratamientos.id, obligatorio |
| fecha_inicio | date | obligatorio |
| fecha_fin | date | obligatorio |
| dosis | str(100) | obligatorio |

### Relaciones

```
Propietario  1 ───< N  Mascota
Mascota      1 ───  1   Historia Clínica
Mascota      1 ───< N  Cita  >─── 1  Veterinario
Mascota      N >───< N  Tratamiento   (vía Mascota–Tratamiento)
```

- Un **propietario** puede tener muchas **mascotas**.
- Cada **mascota** tiene una única **historia clínica**.
- Una **mascota** tiene muchas **citas**; cada cita la atiende un **veterinario**.
- Una **mascota** puede recibir muchos **tratamientos** y un tratamiento se aplica a muchas mascotas (relación N:M resuelta con la tabla `mascota_tratamiento`).

---

## 6. Endpoints

Prefijo base por entidad y estado actual de implementación.

| Entidad | Prefijo | Endpoints implementados | Pendientes |
|---------|---------|--------------------------|------------|
| Home | `/` | `GET /` | — |
| Health | `/health-db` | `GET /health-db` | — |
| Propietarios | `/propietarios` | `POST /` | GET, GET/{id}, PUT, DELETE |
| Veterinarios | `/veterinarios` | `POST /` | GET, GET/{id}, PUT, DELETE |
| Tratamientos | `/tratamientos` | `POST /` | GET, GET/{id}, PUT, DELETE |
| Mascotas | `/mascotas` | `POST /` | GET, GET/{id}, PUT, DELETE |
| Historias clínicas | `/historias-clinicas` | `POST /` | GET, GET/{id}, PUT, DELETE |
| Citas | `/citas` | `POST /` | GET, GET/{id}, PUT, DELETE |
| Mascota–Tratamiento | `/mascotas-tratamientos` | `POST /` | GET, GET/{id}, PUT, DELETE |

> ⚠️ Actualmente **solo está implementada la operación de crear (POST)** en cada entidad. El resto del CRUD está pendiente (ver `PLAN_DE_TRABAJO.md`).

### Documentación interactiva
Con la app levantada:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## 7. Configuración (.env)

La aplicación lee la configuración desde un archivo `.env` en la raíz. Variables necesarias:

```env
APP_NAME=Clinica Veterinaria API
APP_VERSION=1.0.0
APP_DESCRIPTION=API para la gestion de una clinica veterinaria

DB_HOST=localhost
DB_PORT=5432
DB_NAME=clinica_veterinaria
DB_USER=postgres
DB_PASSWORD=tu_password
```

La URL de conexión se construye automáticamente en `settings.py`:
```
postgresql+psycopg://<DB_USER>:<DB_PASSWORD>@<DB_HOST>:<DB_PORT>/<DB_NAME>
```

> El archivo `.env` no se sube al repositorio (está en `.gitignore`). Usa `.env.example` como plantilla.

---

## 8. Puesta en marcha

```bash
# 1. Crear y activar el entorno virtual
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS / Linux

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Crear el archivo .env (copiar de .env.example y rellenar)

# 4. Asegurarse de que PostgreSQL está corriendo y la BD existe

# 5. Levantar el servidor
uvicorn main:app --reload
```

La app crea las tablas automáticamente al arrancar (`Base.metadata.create_all` en el `lifespan` de `main.py`).

Verificar conexión a BD: `GET http://localhost:8000/health-db`

---

## 9. Convenciones del proyecto

- **Idioma del código y la BD**: español (nombres de entidades, campos, tablas).
- **Una clase por capa y entidad**: SRP (responsabilidad única).
- **Sin lógica en `main.py`**: solo crea la app y cablea los routers.
- **Git (Gitflow)**: `main` (estable) + `develop` (integración); ramas `feature/*`.
- **Commits**: en inglés, modo imperativo (`add`, `fix`, `wire`...), concisos.

---

## 10. Estado y próximos pasos

Trabajo pendiente detallado en **[`PLAN_DE_TRABAJO.md`](./PLAN_DE_TRABAJO.md)** y en el [tablero de GitHub Projects](https://github.com/users/DhanaCorredor/projects/7). Resumen:

1. **CRUD completo** (GET, GET/{id}, PUT, DELETE) en las 7 entidades.
2. **Manejo de errores** (404 / validación de claves foráneas).
3. **Carga de datos** desde `datos_clinica.xlsx`.
4. **Tests** con pytest + TestClient.
5. **README** de instalación y uso.
