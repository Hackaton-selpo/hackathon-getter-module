from typing import Optional

from datetime import datetime

from pydantic import BaseModel


class LettersFilter(BaseModel):
    id: Optional[str] = None
    author: Optional[str] = None
    sender: Optional[str] = None
    recipient: Optional[str] = None
    destination: Optional[str] = None
    min_length: Optional[int] = None
    max_length: Optional[int] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None


class Pagination(BaseModel):
    limit: int = 100
    offset: int = 0


class Output(BaseModel):
    text_length: Optional[int] = 200


class LetterData(BaseModel):
    id: str
    date: datetime
    author: str
    text: str
    url: str
    sender: str
    recipient: str
    destination: str

    class Config:
        orm_mode = True
