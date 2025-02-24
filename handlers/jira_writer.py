"""Роутеры для списывания часов в JIRA."""

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from src.services import JiraWriterService


jira_writer_router = Router()
jira_writer_service = JiraWriterService()


class Registration(StatesGroup):
    name = State()
    age = State()


@jira_writer_router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    start_message = jira_writer_service.get_start_message()
    await message.answer(start_message)
    await state.set_state(Registration.name)
