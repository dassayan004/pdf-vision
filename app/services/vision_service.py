from google.cloud import vision
from google.oauth2 import service_account
from PyPDF2 import PdfReader
from io import BytesIO
from app.config import get_settings

settings = get_settings()


def get_vision_client() -> vision.ImageAnnotatorClient:
    credentials = service_account.Credentials.from_service_account_file(
        str(settings.google_application_credentials)
    )
    return vision.ImageAnnotatorClient(credentials=credentials)


def get_pdf_page_count(pdf_content: bytes) -> int:
    reader = PdfReader(BytesIO(pdf_content))
    return len(reader.pages)


def extract_text_from_pdf(pdf_content: bytes) -> list[dict]:
    client = get_vision_client()
    total_pages = get_pdf_page_count(pdf_content)
    # print(f"Total pages in PDF: {total_pages}")

    all_pages = []

    for start in range(1, total_pages + 1, 5):
        end = min(start + 4, total_pages)

        request = vision.AnnotateFileRequest(
            input_config=vision.InputConfig(
                content=pdf_content,
                mime_type="application/pdf",
            ),
            features=[
                vision.Feature(type_=vision.Feature.Type.DOCUMENT_TEXT_DETECTION)
            ],
            pages=list(range(start, end + 1)),
        )

        response = client.batch_annotate_files(requests=[request])

        for file_response in response.responses:
            for i, page_response in enumerate(file_response.responses):
                annotation = page_response.full_text_annotation

                all_pages.append(
                    {
                        "page": start + i,
                        "text": annotation.text if annotation else "",
                    }
                )

    return all_pages
