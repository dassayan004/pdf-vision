from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config import get_settings
from app.routers import extract, health


@asynccontextmanager
async def lifespan(app: FastAPI):
    get_settings()
    yield


settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    description=settings.app_description,
    version=settings.app_version,
    lifespan=lifespan,
)


app.include_router(health.router)
app.include_router(extract.router, tags=["extract"])
