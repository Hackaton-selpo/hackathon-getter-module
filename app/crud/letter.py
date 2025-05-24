from typing import List

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import Letters
from app.schemas import LettersFilter, LetterData


async def get_letters(
    db: AsyncSession,
    filters: LettersFilter,
    text_length: int = 200,
    limit: int = 100,
    offset: int = 0,
) -> List[LetterData]:
    query = select(Letters)

    if filters.id:
        query = query.filter(Letters.id == filters.id)
    if filters.author:
        query = query.filter(Letters.author.ilike(f"%{filters.author}%"))
    if filters.sender:
        query = query.filter(Letters.sender.ilike(f"%{filters.sender}%"))
    if filters.recipient:
        query = query.filter(Letters.recipient.ilike(f"%{filters.recipient}%"))
    if filters.destination:
        query = query.filter(Letters.destination.ilike(f"%{filters.destination}%"))
    if filters.min_length:
        query = query.filter(len(Letters.text) >= filters.min_length)
    if filters.max_length:
        query = query.filter(len(Letters.text) <= filters.max_length)
    if filters.start_date:
        query = query.filter(Letters.date >= filters.start_date)
    if filters.end_date:
        query = query.filter(Letters.date <= filters.end_date)  

    query = query.offset(offset).limit(limit)
    result = await db.execute(query)
    letters = result.unique().scalars().all()

    letter_data_list = [
        LetterData(
            id=letter.id,
            date=letter.date,
            author=letter.author,
            text=letter.text[:text_length+1] if text_length and text_length > 0 else letter.text,
            url=letter.url,
            sender=letter.sender,
            recipient=letter.recipient,
            destination=letter.destination,
        )
        for letter in letters
    ]

    return letter_data_list
