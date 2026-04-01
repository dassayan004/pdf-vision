from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    google_application_credentials: str = ""
    google_sdk_python_logging_scope: str = ""


@lru_cache
def get_settings() -> Settings:
    return Settings()
