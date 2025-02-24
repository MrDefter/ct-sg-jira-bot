"""Точка входа в приложение."""

import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage

from src.handlers import jira_writer_router


def get_token() -> str:
    """Получить токен.

    Returns:
        Токен.
    """
    with open('token', 'r', encoding='utf-8') as file:
        return file.read()


async def main() -> None:
    """Точка входа в приложение."""
    bot = Bot(token=get_token())
    storage = MemoryStorage()
    dispatcher = Dispatcher(storage=storage)

    dispatcher.include_router(jira_writer_router)

    await dispatcher.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
