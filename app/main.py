from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config import get_settings
from app.routers import extract


@asynccontextmanager
async def lifespan(app: FastAPI):
    get_settings()
    yield


app = FastAPI(
    title="PDF Vision API",
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(extract.router, tags=["extract"])
