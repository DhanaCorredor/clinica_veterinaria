# 🐾 Veterinary Clinic API

> REST API for managing a veterinary clinic: owners, pets, veterinarians, appointments, treatments and clinical histories.
> **Factoría F5** project.

📖 **Full wiki on Notion:** [Veterinary Clinic API](https://dhanacorredor.notion.site/API-Cl-nica-Veterinaria-38954980d234801b8a4ffd25266a69fd)

---

## 1. Overview

This API manages the day-to-day operations of a veterinary clinic. It centralizes information about **owners** and their **pets**, the staff (**veterinarians**), the **treatments** offered, scheduled **appointments**, each pet's **clinical history**, and the relationship between pets and the treatments applied to them.

It is built as a **REST API** with automatic interactive documentation (Swagger / OpenAPI).

---

## 2. Tech stack

| Component | Technology |
|-----------|------------|
| Language | Python 3.10+ |
| Web framework | FastAPI |
| ASGI server | Uvicorn |
| ORM | SQLAlchemy 2.0 (`Mapped` / `mapped_column` style) |
| Database | PostgreSQL |
| DB driver | psycopg (binary) |
| Validation | Pydantic + pydantic-settings |
| Configuration | Environment variables via `.env` |

---

## 3. Architecture

The project follows a **layered architecture** with a single responsibility per class. The flow of a request is:

```
HTTP Client
    │
    ▼
Router          → defines the route and HTTP method (endpoint)
    │
    ▼
Validator       → validates/serializes input and output data (Pydantic)
    │
    ▼
Controller      → orchestrates the operation logic
    │
    ▼
Model           → runs the operation against the DB
    │
    ▼
Schema          → object-table mapping (SQLAlchemy ORM)
    │
    ▼
PostgreSQL
```

### What each layer does

- **Router** (`app/routers/`): exposes the HTTP endpoints and delegates to the controller. Contains no business logic.
- **Validator** (`app/schema_validator/`): Pydantic models defining what data comes in (`Create`) and what data goes out (`Response`).
- **Controller** (`app/controllers/`): coordinates the operation; receives the validated data and calls the model.
- **Model** (`app/models/`): contains the methods that talk to the database (`create`, etc.).
- **Schema** (`app/schemas/`): SQLAlchemy classes representing the tables.

---

## 4. Folder structure

```
clinica_veterinaria/
├── app/
│   ├── config/
│   │   └── settings.py              # Configuration (reads .env)
│   ├── controllers/                 # Logic for each entity
│   ├── database/
│   │   └── db_connection.py         # Engine, session and Base
│   ├── models/                      # Database operations
│   ├── routers/                     # HTTP endpoints
│   ├── schema_validator/            # Pydantic validators (input/output)
│   └── schemas/                     # SQLAlchemy tables (ORM)
├── datos_clinica.xlsx               # Sample data to seed the DB
├── Diagrama-veterinaria.drawio      # Entity-relationship diagram
├── main.py                          # Entry point (creates the app and wires routers)
├── requirements.txt
├── .env.example                     # Environment variables template
└── PLAN_DE_TRABAJO.md
```

---

## 5. Data model

The API manages **7 entities**.

### Propietario (Owner)
Owner of one or more pets.

| Field | Type | Constraints |
|-------|------|-------------|
| id | int | PK |
| nombre | str(100) | required |
| correo | str(150) | required |
| telefono | str(20) | required |

### Veterinario (Veterinarian)
Professional who attends appointments.

| Field | Type | Constraints |
|-------|------|-------------|
| id | int | PK |
| nombre | str(100) | required |
| especialidad | str(100) | required |

### Tratamiento (Treatment)
Service or treatment offered by the clinic.

| Field | Type | Constraints |
|-------|------|-------------|
| id | int | PK |
| nombre | str(100) | required |
| tipo | str(100) | required |
| costo | float | required |

### Mascota (Pet)
Animal associated with an owner.

| Field | Type | Constraints |
|-------|------|-------------|
| id | int | PK |
| propietario_id | int | FK → propietarios.id, required |
| nombre | str(100) | required |
| especie | str(50) | required |
| raza | str(50) | required |
| fecha_nacimiento | date | required |

### Historia Clínica (Clinical History)
Unique clinical record for each pet (1:1 relationship).

| Field | Type | Constraints |
|-------|------|-------------|
| id | int | PK |
| mascota_id | int | FK → mascotas.id, **unique**, required |
| peso | float | required |
| observaciones | str(250) | required |

### Cita (Appointment)
Schedule of a pet's visit with a veterinarian.

| Field | Type | Constraints |
|-------|------|-------------|
| id | int | PK |
| mascota_id | int | FK → mascotas.id, required |
| veterinario_id | int | FK → veterinarios.id, required |
| fecha | datetime | required |
| estado | str(50) | required |

### Mascota–Tratamiento (Pet–Treatment)
Junction table (N:M) recording the treatments applied to a pet.

| Field | Type | Constraints |
|-------|------|-------------|
| id | int | PK |
| mascota_id | int | FK → mascotas.id, required |
| tratamiento_id | int | FK → tratamientos.id, required |
| fecha_inicio | date | required |
| fecha_fin | date | required |
| dosis | str(100) | required |

### Relationships

```
Owner        1 ───< N  Pet
Pet          1 ───  1   Clinical History
Pet          1 ───< N  Appointment  >─── 1  Veterinarian
Pet          N >───< N  Treatment   (via Pet–Treatment)
```

- An **owner** can have many **pets**.
- Each **pet** has a single **clinical history**.
- A **pet** has many **appointments**; each appointment is attended by a **veterinarian**.
- A **pet** can receive many **treatments** and a treatment can be applied to many pets (N:M relationship resolved through the `mascota_tratamiento` table).

---

## 6. Endpoints

Base prefix per entity and current implementation status.

| Entity | Prefix | Implemented endpoints | Pending |
|--------|--------|------------------------|---------|
| Home | `/` | `GET /` | — |
| Health | `/health-db` | `GET /health-db` | — |
| Owners | `/propietarios` | `POST /` | GET, GET/{id}, PUT, DELETE |
| Veterinarians | `/veterinarios` | `POST /` | GET, GET/{id}, PUT, DELETE |
| Treatments | `/tratamientos` | `POST /` | GET, GET/{id}, PUT, DELETE |
| Pets | `/mascotas` | `POST /` | GET, GET/{id}, PUT, DELETE |
| Clinical histories | `/historias_clinicas` | `POST /` | GET, GET/{id}, PUT, DELETE |
| Appointments | `/citas` | `POST /` | GET, GET/{id}, PUT, DELETE |
| Pet–Treatment | `/mascota_tratamiento` | `POST /` | GET, GET/{id}, PUT, DELETE |

> ⚠️ Currently **only the create operation (POST)** is implemented for each entity. The rest of the CRUD is pending (see `PLAN_DE_TRABAJO.md`).

### Interactive documentation
With the app running:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## 7. Configuration (.env)

The application reads its configuration from a `.env` file in the root. Required variables:

```env
APP_NAME=Clinica Veterinaria API
APP_VERSION=1.0.0
APP_DESCRIPTION=API para la gestion de una clinica veterinaria

DB_HOST=localhost
DB_PORT=5432
DB_NAME=clinica_veterinaria
DB_USER=postgres
DB_PASSWORD=your_password
```

The connection URL is built automatically in `settings.py`:
```
postgresql+psycopg://<DB_USER>:<DB_PASSWORD>@<DB_HOST>:<DB_PORT>/<DB_NAME>
```

> The `.env` file is not committed to the repository (it is in `.gitignore`). Use `.env.example` as a template.

---

## 8. Getting started

```bash
# 1. Create and activate the virtual environment
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS / Linux

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create the .env file (copy from .env.example and fill it in)

# 4. Make sure PostgreSQL is running and the database exists

# 5. Start the server
uvicorn main:app --reload
```

The app creates the tables automatically on startup (`Base.metadata.create_all` in the `lifespan` of `main.py`).

Check the DB connection: `GET http://localhost:8000/health-db`

---

## 9. Project conventions

- **Code and DB language**: Spanish (entity, field and table names).
- **One class per layer and entity**: SRP (single responsibility).
- **No logic in `main.py`**: it only creates the app and wires the routers.
- **Git (Gitflow)**: `main` (stable) + `develop` (integration); `feature/*` branches.
- **Commits**: English, imperative mood (`add`, `fix`, `wire`...), concise.

---

## 10. Status and next steps

Pending work is detailed in **[`PLAN_DE_TRABAJO.md`](./PLAN_DE_TRABAJO.md)** and on the [GitHub Projects board](https://github.com/users/DhanaCorredor/projects/7). Summary:

1. **Complete CRUD** (GET, GET/{id}, PUT, DELETE) for the 7 entities.
2. **Error handling** (404 / foreign key validation).
3. **Data seeding** from `datos_clinica.xlsx`.
4. **Tests** with pytest + TestClient.
5. **README** for installation and usage.
