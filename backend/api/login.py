"""Работа с API сервиса аутентификации."""

import httpx

from backend.settings import login_settings


class LoginApplicationManager:
    """Работа с API сервиса аутентификации."""
    def __init__(self):
        """Инициализация пути для адреса."""
        url = f'{login_settings.HOST}:{login_settings.PORT}'

        self.__client = httpx.Client()
        self.__login_send_code = f'{url}/login/send_code'
        self.__login_check_code = f'{url}/login/check_code'

    def send_code(self, user_id: str, email: str) -> None:
        """Сгенерировать код и отправить на почту.

        Args:
            user_id: Уникальный идентификаторв пользователя.
            email: Электронная почта пользователя.
        Returns:
            Одноразовый код.
        """
        data_json = {'user_id': user_id, 'email': email}
        self.__client.post(url=self.__login_send_code, json=data_json)

    def check_code(self, user_id: str, code: str) -> dict:
        """Начать аутентификацию (сгенерировать код).

        Args:
            user_id: Уникальный идентификаторв пользователя.
            code: Одноразовый код.
        Returns:
            Одноразовый код.
        """
        data_json = {'user_id': user_id, 'code': code}
        response = self.__client.post(url=self.__login_check_code, json=data_json)

        return response.json()