"""Модуль, предоставляющий маршруты (роуты) для работы с письмами.

Содержит готовый роутер для подключения к основному FastAPI-приложению.
"""

from .letters import router as letters_router
from .images import router as images_router

__all__ = ["letters_router", "images_router"]
