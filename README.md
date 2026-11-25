# Axity Python Labs

Repositorio destinado al desarrollo y entrega de los laboratorios prácticos del **curso de Python de Axity**.

## Objetivo

Fortalecer los conocimientos en Python mediante proyectos independientes, aplicando buenas prácticas de desarrollo, pruebas automatizadas, patrones de diseño y arquitectura de software.

## Organización

El curso está dividido en tres niveles: Fundamental, Intermediate y Advanced.

Cada módulo puede contener uno o varios laboratorios. Cada laboratorio se desarrollará como un proyecto Python independiente, con sus propias dependencias, código fuente, pruebas y documentación.

### Fundamental Level

| Módulo | Laboratorio | Proyecto |
|---|---|---|
| 01. Entorno y herramientas | Crear proyecto con Poetry, entorno virtual e instalar Black/isort/Ruff | `lab-01-01-poetry-environment` |
| 01 | Configurar pre-commit y corregir infracciones PEP 8 | `lab-01-02-precommit-pep8` |
| 02. Fundamentos del lenguaje | Lectura y filtrado de datos JSON | `lab-02-01-json-processing` |
| 02 | Agregación de datos y manejo de errores de archivo/formato | `lab-02-02-json-error-handling` |
| 03. Funciones y programación Pythonic | Decorador de reintentos con backoff | `lab-03-01-retry-decorator` |
| 03 | Generador por lotes y context manager de temporización | `lab-03-02-batch-timer` |
| 04. Objetos y modelos de datos | Dataclass Order con cálculos y comparaciones | `lab-04-01-order-dataclass` |
| 04 | Modelos Pydantic OrderIn/OrderOut y conversión a entidad | `lab-04-02-order-pydantic` |
| 05. Tipado estático y calidad | Type hints, mypy y Ruff sobre código previo | `lab-05-01-static-typing` |
| 05 | Configuración de pre-commit | `lab-05-02-precommit` |
| 06. Librería estándar y E/S | Ingesta de CSV, métricas y exportación JSON | `lab-06-01-csv-metrics` |
| 06 | Logging con distintos niveles | `lab-06-02-logging` |
| 07. HTTP y consumo de APIs | Cliente HTTPX con reintentos y timeouts | `lab-07-01-http-client` |
| 07 | Descarga por streaming a disco | `lab-07-02-http-streaming` |

### Intermediate Level

| Módulo | Laboratorio | Proyecto |
|---|---|---|
| 08. Acceso a datos y ORM | Modelos User/Order/OrderItem y CRUD | `lab-08-01-sqlalchemy-crud` |
| 08 | Migración Alembic y pruebas SQLite en memoria | `lab-08-02-alembic-sqlite` |
| 09. APIs web con FastAPI | CRUD de Orders con validación | `lab-09-01-fastapi-orders` |
| 09 | Login JWT y pruebas de integración | `lab-09-02-jwt-integration` |
| 10. Pruebas y TDD | Implementación de historia con TDD | `lab-10-01-tdd` |
| 10 | Property-based testing y cobertura | `lab-10-02-property-testing` |
| 11. Concurrencia y rendimiento | Fetcher concurrente con HTTPX y comparación síncrona | `lab-11-01-async-fetcher` |
| 11 | Cálculo CPU-bound con ProcessPoolExecutor | `lab-11-02-process-pool` |
| 12. Principios SOLID | Refactor mediante Protocol e implementaciones memoria/SQL | `lab-12-01-dependency-inversion` |
| 12 | Verificación de LSP | `lab-12-02-lsp` |
| 13. Patrones de diseño | Strategy para precios | `lab-13-01-strategy` |
| 13 | Decorator de caché | `lab-13-02-cache-decorator` |
| 13 | Adapter para proveedor externo y pruebas | `lab-13-03-adapter` |
| 14. Ciencia de datos | Carga y limpieza de CSV en Pandas | `lab-14-01-data-cleaning` |
| 14 | Entrenar clasificador, guardar modelo y probar inferencia | `lab-14-02-classification` |
| 15. Arquitectura Hexagonal | CreateOrder con puerto y adaptadores memoria/SQLAlchemy | `lab-15-01-create-order` |
| 15 | Notificación HTTP simulada y pruebas de contrato | `lab-15-02-notification-adapter` |

### Advanced Level

| Módulo | Laboratorio | Proyecto |
|---|---|---|
| 16. Arquitectura Limpia | Reestructuración de Orders con UoW y Presenter | `lab-16-01-clean-architecture` |
| 16 | Evento OrderCreated manejado en aplicación | `lab-16-02-domain-events` |
| 17. Empaquetado y CI/CD | Generación de wheel y Dockerfile multistage | `lab-17-01-packaging-docker` |
| 17 | Workflow CI y publicación en registry | `lab-17-02-ci-pipeline` |
| 18. CLI y automatización | CLI con Typer para gestionar Orders y entry point | `lab-18-01-orders-cli` |
| 19. Seguridad y mantenimiento | Pydantic Settings y auditoría de dependencias | `lab-19-01-dependency-security` |
| 19 | Docker sin root y permisos mínimos | `lab-19-02-docker-hardening` |
| 20. Interoperabilidad (opcional) | Protobuf, servidor y cliente gRPC | `lab-20-01-grpc` |
| 20 | Publicación de OrderCreated con RabbitMQ/Redis | `lab-20-02-messaging` |

## Estructura del repositorio

```text
axity-python-labs/
├── README.md
├── .gitignore
│
├── fundamental/
│   ├── module-01-environment/
│   │   ├── lab-01-01-poetry-environment/
│   │   └── lab-01-02-precommit-pep8/
│   ├── module-02-language-basics/
│   │   ├── lab-02-01-json-processing/
│   └── ...
│
├── intermediate/
│   ├── module-08-database-orm/
│   │   ├── lab-08-01-sqlalchemy-crud/
│   └── ...
│
└── advanced/
    ├── module-16-clean-architecture/
    │   ├── lab-16-01-clean-architecture/
    └── ...
```

## Estructura de cada laboratorio

Cada proyecto tendrá su propia configuración:

```text
lab-xx-xx-name/
├── README.md
├── pyproject.toml
├── poetry.lock
├── src/
└── tests/
```

Los archivos de configuración adicionales dependerán de los requisitos de cada laboratorio.

## Tecnologías y herramientas

- **Python:** 3.12
- **Gestión de dependencias:** Poetry
- **Calidad:** Black, isort, Ruff, mypy y pre-commit
- **Testing:** pytest, unittest.mock y Hypothesis
- **APIs:** FastAPI, HTTPX y Pydantic
- **Persistencia:** SQLite, PostgreSQL, SQLAlchemy y Alembic
- **Arquitectura:** SOLID, patrones de diseño, arquitectura hexagonal y limpia
- **DevOps:** Docker, GitHub Actions y Azure
- **Ciencia de datos:** Pandas, NumPy y scikit-learn

## Ejecución

Cada laboratorio se ejecuta de manera independiente.

```bash
cd fundamental/module-01-environment/lab-01-01-poetry-environment
poetry install
poetry run python --version
```

## Buenas prácticas

- Utilizar Python 3.12.
- Mantener dependencias independientes por laboratorio.
- Versionar `pyproject.toml` y `poetry.lock`.
- Excluir `.venv`, cachés y archivos temporales de Git.
- Aplicar PEP 8 y PEP 20.
- Documentar cada laboratorio.
- Incorporar pruebas automatizadas cuando corresponda.

## Proyecto integrador

El proyecto final se desarrollará en un repositorio independiente:

[axity-python-integrator](https://github.com/jsvictordev/axity-python-integrator)

## Autor

**Víctor José**

Capacitación Python | Axity