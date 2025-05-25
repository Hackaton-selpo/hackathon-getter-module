"""Основной модуль приложения.

Модуль инициализирует приложение FastAPI, настраивает менеджер жизненного цикла,
а также подключает маршруты.
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.api.v1 import letters_router
from app.db.database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Асинхронный контекстный менеджер для управления событиями жизненного цикла.

    Вызывается при запуске приложения для инициализации базы данных,
    после чего передаёт управление, пока приложение работает.

    Args:
        app (FastAPI): Экземпляр приложения FastAPI.

    Yields:
        None
    """
    await init_db()
    yield


app = FastAPI(
    title="Letters Getter API",
    description="""API для получения данных о фронтовых письмах.

xKamysh is the best""",
    version="1.0.0",
    lifespan=lifespan,
    root_path_in_servers=True,
    root_path="/letters",
)


@app.get("/", include_in_schema=False)
async def root_redirect():
    """Корневой маршрут, который перенаправляет пользователя на страницу документации.

    Returns:
        RedirectResponse: Ответ, перенаправляющий на страницу /docs.
    """
    return RedirectResponse(url="/docs")


app.include_router(letters_router, prefix="/letters", tags=["letters"])
