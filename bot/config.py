from functools import lru_cache

from pydantic import EmailStr, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    # Tutorium creds
    tutorium_email: EmailStr = Field(..., alias="TUTORIUM_EMAIL", description="Tutorium user email")
    tutorium_password: str = Field(..., min_length=8, alias="TUTORIUM_PASSWORD", description="Tutorium user password")

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


@lru_cache
def get_config() -> Config:
    return Config()
