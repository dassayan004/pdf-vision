---
name: pdf-vision project overview
description: FastAPI API for PDF text extraction using Google Cloud Vision OCR, managed with uv, Python 3.12
type: project
---

pdf-vision is a FastAPI API that extracts text from PDFs using Google Cloud Vision's DOCUMENT_TEXT_DETECTION. Managed with uv (Python 3.12).

**Key components:**
- `app/main.py` — FastAPI app with lifespan, loads settings on startup
- `app/config.py` — Pydantic settings from `.env` (Google credentials)
- `app/routers/extract.py` — `POST /extract` accepts PDF uploads, returns per-page text
- `app/services/vision_service.py` — Google Cloud Vision integration for OCR
- `app/dto/extract_dto.py` — Response models (`ExtractResponse`, `PageData`)

**Dependencies:** fastapi[standard], google-cloud-vision

**How to apply:** Use uv for dependency management (`uv add`, `uv run`). Run the app with `uv run fastapi dev app/main.py`.
