from fastapi import APIRouter, File, HTTPException, UploadFile

from app.dto.extract_dto import ExtractResponse, PageData
from app.services.vision_service import extract_text_from_pdf

router = APIRouter()


@router.post("/extract", response_model=ExtractResponse)
def extract_pdf(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="File must be a PDF")

    content = file.file.read()
    try:
        pages = extract_text_from_pdf(content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return ExtractResponse(
        filename=file.filename,
        pages=len(pages),
        data=[PageData(**p) for p in pages],
    )
