"""Конечный автомат регистрации пользователя."""

from aiogram.fsm.state import State, StatesGroup


class LoginState(StatesGroup):
    """Конечный автомат авторизации пользователя."""
    send_code = State()
    check_code = State()
