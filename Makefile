.DEFAULT_GOAL := help

.PHONY: help install dev prod lint format clean

APP = app/main.py
PY_DIRS = app
help:
	@printf "Available targets:\n"
	@printf "  help     Show this help message\n"
	@printf "  install  Install project dependencies\n"
	@printf "  dev      Run the FastAPI development server\n"
	@printf "  prod     Run the FastAPI production server\n"
	@printf "  format       Format source and test files\n"
	@printf "  lint         Run Ruff checks\n"
	@printf "  lint-fix     Run Ruff checks and apply fixes\n"
	@printf "  check        Run all checks and tests\n"
	@printf "  clean        Remove caches and build artifacts\n"

install:
	uv sync

dev:
	uv run fastapi dev $(APP)

prod:
	uv run fastapi run $(APP)

format:
	uv run isort $(PY_DIRS)
	uv run black $(PY_DIRS)

lint:
	uv run ruff check $(PY_DIRS)

lint-fix:
	uv run ruff check $(PY_DIRS) --fix

check:
	uv run black --check $(PY_DIRS)
	uv run isort --check-only $(PY_DIRS)
	uv run ruff check $(PY_DIRS)

clean:
	find . -type d \( -name __pycache__ -o -name .pytest_cache -o -name .ruff_cache -o -name htmlcov \) -prune -exec rm -rf {} +
	find . -type f \( -name "*.pyc" -o -name ".coverage" \) -delete
