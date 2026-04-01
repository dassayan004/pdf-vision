from pydantic import BaseModel


class PageData(BaseModel):
    page: int
    text: str


class ExtractResponse(BaseModel):
    filename: str | None
    pages: int
    data: list[PageData]
