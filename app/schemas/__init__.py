"""Пакет моделей данных для работы с письмами.

Этот модуль предоставляет модели, используемые для фильтрации, пагинации,
форматирования вывода и представления данных о письмах.
"""

from .letter import LetterData, LettersFilter, Output, Pagination

__all__ = ["LettersFilter", "Pagination", "Output", "LetterData"]
