"""Модуль базы данных.

Содержит базовый класс моделей, зависимости для получения сессии,
а также функции инициализации базы данных.
"""

from .database import Base, get_session, init_db

__all__ = ["get_session", "init_db", "Base"]
