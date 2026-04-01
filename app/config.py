from functools import lru_cache

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # =========================
    # App Static Config
    # =========================
    app_name: str = "PDF Vision API"
    app_title: str = "PDF Vision"
    app_description: str = (
        "A PDF extraction service powered by Google Cloud Vision API."
    )
    app_version: str = "0.1.0"

    # =========================
    # Environment Variables
    # =========================
    google_application_credentials: str = Field(
        default="",
        validation_alias="GOOGLE_APPLICATION_CREDENTIALS",
    )
    google_sdk_python_logging_scope: str = Field(
        default="",
        validation_alias="GOOGLE_SDK_PYTHON_LOGGING_SCOPE",
    )

    @field_validator(
        "google_application_credentials", "google_sdk_python_logging_scope"
    )
    @classmethod
    def validate_not_empty(cls, v: str, info) -> str:
        if not v or not v.strip():
            raise ValueError(f"{info.field_name} must not be empty or whitespace")
        return v

    # =========================
    # Config
    # =========================
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


# =========================
# Cached instance (singleton)
# =========================
@lru_cache
def get_settings() -> Settings:
    return Settings()
