"""Роутеры для списывания часов в JIRA."""

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from src.services import JiraWriterService


jira_writer_router = Router()
jira_writer_service = JiraWriterService()


@jira_writer_router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer('Привет! Я бот для списывания часов с искуственным интелектом.')
