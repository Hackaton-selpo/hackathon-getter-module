from typing import List, Optional

from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import get_letters
from app.db import get_session
from app.schemas import LettersFilter, LetterData

class LettersAPI:
    def __init__(self):
        self.router = APIRouter()

        # Регистрация маршрутов
        self.router.get("/", response_model=List[LetterData])(self.list_letters)

    async def list_letters(
        self,
        letter_id: Optional[str] = Query(None),
        author: Optional[str] = Query(None),
        sender: Optional[str] = Query(None),
        recipient: Optional[str] = Query(None),
        destination: Optional[str] = Query(None),
        min_length: Optional[int] = Query(0, ge=0),
        max_length: Optional[int] = Query(None, ge=10),
        start_date: Optional[datetime] = Query(None),
        end_date: Optional[datetime] = Query(None),
        text_length: int = Query(None),
        limit: int = Query(100, le=100),
        offset: int = Query(0, ge=0),
        db: AsyncSession = Depends(get_session),
    ):
        try:
            filters = LettersFilter(
                id=letter_id,
                author = author,
                sender = sender,
                recipient = recipient,
                destination = destination,
                min_length = min_length,
                max_length = max_length,
                start_date = start_date,
                end_date = end_date,
            )
            letters = await get_letters(db, filters, text_length=text_length, limit=limit, offset=offset)
            return letters
        except Exception:
            raise HTTPException(status_code=500, detail="Internal server error")
