import os

from google.cloud import vision

from app.config import get_settings

settings = get_settings()
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = settings.google_application_credentials
os.environ["GOOGLE_SDK_PYTHON_LOGGING_SCOPE"] = settings.google_sdk_python_logging_scope


def extract_text_from_pdf(pdf_content: bytes) -> list[dict]:
    client = vision.ImageAnnotatorClient()

    input_config = vision.InputConfig(
        content=pdf_content,
        mime_type="application/pdf",
    )
    feature = vision.Feature(type_=vision.Feature.Type.DOCUMENT_TEXT_DETECTION)
    request = vision.AnnotateFileRequest(
        input_config=input_config,
        features=[feature],
    )

    response = client.batch_annotate_files(requests=[request])

    pages = []
    for file_response in response.responses:
        for i, page_response in enumerate(file_response.responses):
            annotation = page_response.full_text_annotation
            pages.append(
                {
                    "page": i + 1,
                    "text": annotation.text if annotation else "",
                }
            )

    return pages
