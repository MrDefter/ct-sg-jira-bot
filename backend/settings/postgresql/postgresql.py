"""Настройки для базы данных PostgreSQL."""

from functools import cache

from pydantic_settings import BaseSettings
from pydantic import Field


class PostgreSQLSettings(BaseSettings):
    """Настройки для базы данных PostgreSQL."""
    HOST: str = Field(
        description='Хост для базы данных PostgreSQL.',
        examples=['127.0.0.1'],
    )
    PORT: int = Field(
        description='Порт для базы данных PostgreSQL.',
        examples=[5432]
    )
    USER: str = Field(
        description='Пользователь базы данных PostgreSQL.',
        examples=['user'],
    )
    PASSWORD: str = Field(
        description='Пароль базы данных PostgreSQL.',
        examples=['password'],
    )
    DATABASE: str = Field(
        description='Название базы данных PostgreSQL.',
        examples=['postgres'],
    )

    class Config:
        env_prefix = 'POSTGRESQL_'
        frozen = True


@cache
def get_postgresql_settings() -> PostgreSQLSettings:
    """Получить настройки для базы данных PostgreSQL."""
    return PostgreSQLSettings()
