# Architecture & Tech Stack

## Chosen Tech Stack (recommended)

- Language: Python 3.14
- Web/API framework: FastAPI (async, OpenAPI support)
- Data layer: SQLAlchemy (ORM) + Alembic (migrations)
- Database (dev): SQLite; (prod): PostgreSQL
- Background jobs: RQ or Celery (optional, depending on workload)
- Authentication: JSON Web Tokens (JWT) or OAuth2 (FastAPI utilities)
- Tests: pytest
- Linting / formatting: flake8 or ruff, black/isort
- Packaging / deps: `pyproject.toml` (Poetry or pip-tools) or `requirements.txt`
- Containerization: Docker + docker-compose for local dev
- CI: GitHub Actions (tests, lint, build, optional push to registry)

## High-level Architecture

- Clients: web browsers or CLI tools that call the API.
- API Layer: FastAPI application exposing REST/JSON endpoints and OpenAPI docs.
- Persistence: relational DB (Postgres in production). The API uses SQLAlchemy models.
- Background Worker (optional): processes long-running tasks, communicates via Redis.
- File Storage (if needed): local storage for dev, S3-compatible for production.
- CI/CD: GH Actions run tests and linters; a build step creates Docker image for deployment.

Flow:
1. Client → FastAPI (HTTP)
2. FastAPI validates request → business logic → DB read/write
3. For long tasks: FastAPI enqueues job → Worker consumes job → updates DB / storage
4. Responses returned to client; observability via logs + (optional) metrics/tracing

## Architectural Decisions & Rationale

- FastAPI chosen for developer productivity, async support and built-in OpenAPI.
- SQLAlchemy + Alembic provide a stable migration and ORM story across SQLite/Postgres.
- Start with SQLite for quick local setup; move to Postgres for concurrency and production needs.
- Use Docker to ensure reproducible dev and CI environments.

## Next Actions

- Scaffold project with `src/`, `tests/`, `docs/`, `scripts/`, `Dockerfile`, and `pyproject.toml`.
- Implement minimal FastAPI app and one sample endpoint to validate the pipeline.

