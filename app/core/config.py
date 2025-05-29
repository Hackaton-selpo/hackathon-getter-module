"""Модуль конфигурации приложения.

Содержит класс Config для загрузки настроек из переменных окружения.
Позволяет управлять параметрами базы данных, пагинацией и внешними ресурсами.
"""

from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    """Класс конфигурации приложения.

    Загружает настройки из .env файла и предоставляет:
        - Параметры подключения к PostgreSQL

    Attributes:
        POSTGRES_HOST (str): Хост PostgreSQL сервера.
        POSTGRES_PORT (int): Порт PostgreSQL сервера.
        POSTGRES_DB (str): Имя базы данных PostgreSQL.
        POSTGRES_USER (str): Имя пользователя для подключения к БД.
        POSTGRES_PASSWORD (str): Пароль пользователя БД.
        POSTGRES_URL (str): Строка подключения к PostgreSQL (автогенерация).
    """

    # Настройки PostgreSQL
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    users_db_user: str
    users_db_databasename: str
    users_db_host: str
    users_db_port: str

    @property
    def POSTGRES_URL(self) -> str:
        """Генерирует строку подключения к БД на основе параметров.

        Returns:
            str: Строка подключения к БД.
        """
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    # Конфигурация загрузки переменных окружения
    model_config = ConfigDict(env_file=".env")  # type: ignore
    # _ = model_config  # type: ignore


# Единственный экземпляр конфигурации, используемый в приложении
config: Config = Config()  # type: ignore[call-arg]
