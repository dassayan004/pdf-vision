# PDF Vision

A PDF extraction service powered by Google Cloud Vision API.

## Tech Stack

<p>
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/Google%20Cloud%20Vision-4285F4?logo=googlecloud&logoColor=white" alt="Google Cloud Vision" />
  <img src="https://img.shields.io/badge/uv-DE5FE9?logo=uv&logoColor=white" alt="uv" />
  <img src="https://img.shields.io/badge/Ruff-D7FF64?logo=ruff&logoColor=black" alt="Ruff" />
  <img src="https://img.shields.io/badge/Black-000000?logo=python&logoColor=white" alt="Black" />
</p>

## Prerequisites

- [Python 3.12+](https://www.python.org/downloads/)
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- A Google Cloud service account JSON key with Vision API enabled

## Setup

```bash
# Clone the repository
git clone <repo-url> && cd pdf-vision

# Install dependencies
make install

# Configure environment
cp .env.example .env
# Edit .env and set GOOGLE_APPLICATION_CREDENTIALS to your service account JSON key path
```

## Running

```bash
# Development server (hot reload)
make dev

# Production server
make prod
```

## Scripts

| Command          | Description                              |
| ---------------- | ---------------------------------------- |
| `make install`   | Install project dependencies via uv      |
| `make dev`       | Start FastAPI dev server with hot reload  |
| `make prod`      | Start FastAPI production server           |
| `make format`    | Format code with isort and Black          |
| `make lint`      | Run Ruff linter checks                   |
| `make lint-fix`  | Run Ruff checks and auto-fix issues      |
| `make check`     | Run all checks (Black, isort, Ruff)      |
| `make clean`     | Remove caches and build artifacts        |
