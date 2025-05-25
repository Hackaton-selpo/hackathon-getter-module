"""Модуль моделей базы данных.

Содержит ORM-модели, используемые для работы с таблицами в базе данных.
"""

from sqlalchemy import Column, DateTime, String

from app.db.database import Base


class Letters(Base):
    """ORM-модель, представляющая таблицу писем в базе данных.

    Attributes:
        id (str): Уникальный идентификатор письма. Первичный ключ.
        date (datetime): Дата и время создания письма.
        author (str): Автор письма.
        text (str): Текст письма.
        url (str): Ссылка на источник или полный текст письма.
        sender (str): Отправитель письма.
        recipient (str): Получатель письма.
        destination (str): Место назначения письма.
    """

    __tablename__ = "letters"

    id = Column(String, primary_key=True)
    date = Column(DateTime)
    author = Column(String)
    text = Column(String)
    url = Column(String)
    sender = Column(String)
    recipient = Column(String)
    destination = Column(String)
