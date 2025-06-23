"""Сервис для списывания часов в JIRA."""

import textwrap

from backend.api import LoginApplicationManager


class LoginService:
    """Сервис для входа."""
    def __init__(self) -> None:
        """Иницализация необходимых классов."""
        self.__login_application_manager = LoginApplicationManager()

    @staticmethod
    def cmd_start() -> str:
        """Обработчик роутера cmd_help.

        Returns:
            Сообщение обработчика cmd_help.
        """
        response_message = '''
        Привет!
        Я бот для списывания часов с искуственным интеллектом.
        Для авторизации напиши команду /login.
        Для помощи по функционалу бота напиши команду /help.
        '''
        return textwrap.dedent(response_message)

    @staticmethod
    def cmd_start_login() -> str:
        """Обработчик роутера cmd_start_login.

        Returns:
            Сообщение обработчика cmd_start_login.
        """
        return textwrap.dedent('Введите пожалуйста свой email.')

    def cmd_send_code(self, user_id: str, email: str) -> str:
        """Обработчик роутера cmd_send_email.

        Args:
            user_id: Уникальный идентификатор пользователя.
            email: Электронная почта пользователя.
        Returns:
            Сообщение обработчика cmd_send_email.
        """
        self.__login_application_manager.send_code(user_id=user_id, email=email)
        return textwrap.dedent('Одноразовый код отправлен на вашу почту.')

    def cmd_check_code(self, user_id: str, code: str) -> str:
        """Обработчик роутера cmd_check_code.

        Args:
            user_id: Уникальный идентификатор пользователя.
            code: Одноразовый код для проверки.
        """
        code_data = self.__login_application_manager.check_code(user_id=user_id, code=code)
        if code_data['completed_flag']:
            return textwrap.dedent('Успешная авторизация.')
        else:
            return textwrap.dedent('Одноразовый код не совпадает.')
