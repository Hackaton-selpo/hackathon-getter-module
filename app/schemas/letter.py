"""Модуль, содержащий модели данных для работы с письмами (letters).

Включает модели для фильтрации, пагинации, вывода и основных данных о письмах.
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class LettersFilter(BaseModel):
    """Модель фильтров для поиска писем.

    Attributes:
        id (Optional[str]): Идентификатор письма.
        author (Optional[str]): Автор письма.
        sender (Optional[str]): Отправитель письма.
        recipient (Optional[str]): Получатель письма.
        destination (Optional[str]): Место назначения письма.
        min_length (Optional[int]): Минимальная длина текста письма.
        max_length (Optional[int]): Максимальная длина текста письма.
        start_date (Optional[datetime]): Начальная дата создания письма.
        end_date (Optional[datetime]): Конечная дата создания письма.
    """

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
    """Модель параметров пагинации.

    Attributes:
        limit (int): Максимальное количество возвращаемых записей. По умолчанию 100.
        offset (int): Смещение от начала списка. По умолчанию 0.
    """

    limit: int = 100
    offset: int = 0


class Output(BaseModel):
    """Модель параметров вывода данных о письме.

    Attributes:
        text_length (Optional[int]): Максимальная длина текста письма в ответе.
                                     По умолчанию 200 символов.
    """

    text_length: Optional[int] = 200


class LetterData(BaseModel):
    """Модель данных одного письма.

    Attributes:
        id (str): Уникальный идентификатор письма.
        date (datetime): Дата и время создания письма.
        author (str): Автор письма.
        text (str): Текст письма.
        url (str): Ссылка на полный текст или ресурс с письмом.
        sender (str): Отправитель письма.
        recipient (str): Получатель письма.
        destination (str): Место назначения письма.
    """

    id: str
    date: datetime
    author: str
    text: str
    url: str
    sender: str
    recipient: str
    destination: str

    model_config = {"from_attributes": True}
