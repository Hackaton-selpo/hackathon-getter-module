"""Модуль API для работы с письмами.

Содержит маршруты (роуты) и обработчики для получения данных о письмах.
"""

from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import get_letters
from app.db import get_session
from app.schemas import LetterData, LettersFilter

# Создаем роутер
router = APIRouter()


@router.get("/", response_model=List[LetterData])
async def list_letters(
    letter_id: Optional[str] = Query(
        None, description="Уникальный идентификатор письма"
    ),
    author: Optional[str] = Query(
        None, description="Имя автора письма (поиск по частичному совпадению)"
    ),
    sender: Optional[str] = Query(
        None, description="Имя отправителя (поиск по частичному совпадению)"
    ),
    recipient: Optional[str] = Query(
        None, description="Имя получателя (поиск по частичному совпадению)"
    ),
    destination: Optional[str] = Query(
        None, description="Место назначения (поиск по частичному совпадению)"
    ),
    min_length: Optional[int] = Query(
        0, ge=0, description="Минимальная длина текста письма"
    ),
    max_length: Optional[int] = Query(
        None, ge=10, description="Максимальная длина текста письма"
    ),
    start_date: Optional[datetime] = Query(
        None, description="Начальная дата создания письма"
    ),
    end_date: Optional[datetime] = Query(
        None, description="Конечная дата создания письма"
    ),
    text_length: int = Query(
        None,
        description="Длина текста письма в ответе",
    ),
    limit: int = Query(100, le=100, description="Количество возвращаемых записей"),
    offset: int = Query(0, ge=0, description="Смещение от начала списка"),
    db: AsyncSession = Depends(get_session),
):
    """Обработчик запроса для получения списка писем с настройками вывода."""
    try:
        filters = LettersFilter(
            id=letter_id,
            author=author,
            sender=sender,
            recipient=recipient,
            destination=destination,
            min_length=min_length,
            max_length=max_length,
            start_date=start_date,
            end_date=end_date,
        )
        letters = await get_letters(
            db, filters, text_length=text_length, limit=limit, offset=offset
        )
        return letters
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")
