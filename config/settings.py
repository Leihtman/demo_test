import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=f".env/{os.environ['env_file_name']}")
    base_url: str


def get_settings():
    return Settings()
