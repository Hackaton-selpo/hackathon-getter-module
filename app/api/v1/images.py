"""Модуль API для работы с письмами.

Содержит маршруты (роуты) и обработчики для получения данных о письмах.
"""

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.v1.schemas import Resp
from app.crud.images import fetch_data_with_limit_offset
from app.db import get_session

# Создаем роутер
router = APIRouter()


@router.get(
    "/images",
    response_model=list[Resp],
)
async def list_letters(
    limit: int = Query(100, le=100, description="Количество возвращаемых записей"),
    offset: int = Query(0, ge=0, description="Смещение от начала списка"),
    db: AsyncSession = Depends(get_session),
):
    """Обработчик запроса для получения списка писем с настройками вывода."""

    letters = await fetch_data_with_limit_offset(
        type_of_data="image", limit=limit, offset=offset
    )

    return letters


@router.get(
    "/audios",
    response_model=list[Resp],
)
async def list_letters(
    limit: int = Query(100, le=100, description="Количество возвращаемых записей"),
    offset: int = Query(0, ge=0, description="Смещение от начала списка"),
    db: AsyncSession = Depends(get_session),
):
    """Обработчик запроса для получения списка писем с настройками вывода."""

    letters = await fetch_data_with_limit_offset(
        type_of_data="audio", limit=limit, offset=offset
    )

    return letters
