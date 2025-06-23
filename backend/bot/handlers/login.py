"""Роутеры для списывания часов в JIRA."""

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext


from backend.bot.services import LoginService
from backend.bot.state_group import LoginState


login_router = Router()
login_service = LoginService()


@login_router.message(Command("start"))
async def cmd_start(message: Message):
    """Команда для старта.

    Args:
        message: Объект сообщения пользователя.
    """
    response_message = login_service.cmd_start()

    await message.answer(response_message)


@login_router.message(Command('login'))
async def cmd_start_login(message: Message, state: FSMContext):
    """Команда для ввода почты.

    Args:
        message: Объект сообщения пользователя.
        state: Конечный автомат авторизации.
    """
    response_message = login_service.cmd_start_login()

    await message.answer(response_message)
    await state.set_state(LoginState.send_code)


@login_router.message(LoginState.send_code)
async def cmd_send_code(message: Message, state: FSMContext):
    """Команда для отправки одноразового кода.

    Args:
        message: Объект сообщения пользователя.
        state: Конечный автомат авторизации.
    """
    response_message = login_service.cmd_send_code(user_id=str(message.from_user.id), email=message.text)

    await message.answer(response_message)
    await state.set_state(LoginState.check_code)


@login_router.message(LoginState.check_code)
async def cmd_check_code(message: Message, state: FSMContext):
    """Команда для проверки одноразового кода.

    Args:
        message: Объект сообщения пользователя.
        state: Конечный автомат авторизации.
    """
    response_message = login_service.cmd_check_code(user_id=str(message.from_user.id), code=message.text)

    await message.answer(response_message)
