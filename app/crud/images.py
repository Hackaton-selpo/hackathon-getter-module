import asyncpg
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()


async def fetch_data_with_limit_offset(
    type_of_data: str, limit: int = None, offset: int = None
):
    # Подключение к базе данных
    conn = await asyncpg.connect(
        user=os.getenv("USERS_DB_USER"),
        password=os.getenv("USERS_DB_PASSWORD"),
        database=os.getenv("USERS_DB_DATABASENAME"),
        host=os.getenv("USER_DB_HOST"),
        port=os.getenv("USERS_DB_PORT"),
    )

    try:
        # Пример SQL-запроса с LIMIT и OFFSET
        query = f"""
        SELECT *
        FROM messages
        INNER JOIN messages_types ON messages_types.id = messages.message_type_id
        WHERE messages_types.name ='{type_of_data}'
        """
        if limit and offset:
            query += "  LIMIT $1 OFFSET $2"

            # Выполнение запроса
            records = await conn.fetch(query, limit, offset)
        else:
            records = await conn.fetch(query)
        # Преобразование записей в список словарей (если нужно)
        result = [dict(record) for record in records]

        return result
    finally:
        # Закрытие соединения
        await conn.close()


# Пример использования
async def main():
    data = await fetch_data_with_limit_offset(type_of_data="image")
    for row in data:
        print(row)


if __name__ == "__main__":
    asyncio.run(main())
