from functools import lru_cache
from pathlib import Path

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )
    google_application_credentials: Path = Path()
    google_sdk_python_logging_scope: str = ""

    @field_validator("google_application_credentials")
    @classmethod
    def validate_credentials(cls, v: Path) -> Path:
        if not v or v == Path():
            raise ValueError(
                "GOOGLE_APPLICATION_CREDENTIALS is required. "
                "Set it in your .env file to the path of your service account JSON key."
            )
        if not v.is_file():
            raise ValueError(f"Credentials file not found: {v}")
        return v


@lru_cache
def get_settings() -> Settings:
    return Settings()
