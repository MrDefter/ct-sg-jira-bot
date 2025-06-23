"""Настройки для базы данных PostgreSQL."""

from functools import cache

from pydantic_settings import BaseSettings
from pydantic import Field


class LoginSettings(BaseSettings):
    """Настройки для базы данных PostgreSQL."""
    HOST: str = Field(
        description='Хост для базы данных PostgreSQL.',
        examples=['127.0.0.1'],
    )
    PORT: int = Field(
        description='Порт для базы данных PostgreSQL.',
        examples=[8001]
    )

    class Config:
        env_prefix = 'LOGIN_SERVICE_'
        frozen = True


@cache
def get_login_settings() -> LoginSettings:
    """Получить настройки для базы данных PostgreSQL."""
    return LoginSettings()


login_settings = get_login_settings()
