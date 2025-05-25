# ✉️ Letters Getter Module

**Letters Getter Module** — асинхронное приложение для обработки данных о фронтовых письмах с сайта [pismapobedy.ru](https://pismapobedy.ru/letters).

## 📦 Технологии

- [Python 3.12+](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/#installation) — управление зависимостями
- [PostgreSQL](https://www.postgresql.org/) — хранение спаршенных данных
- [FastAPI](https://fastapi.tiangolo.com/) — API для получения данных
- [SQLAlchemy ORM](https://docs.sqlalchemy.org/en/20/orm/) — работа с БД
- [Taskfile](https://taskfile.dev/) — автоматизация задач (опционально)

## 🛠️ Установка и запуск

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/Hackaton-selpo/hackathon-getter-module
cd hackathon-getter-module
```

### 2. Установите зависимости

```bash
poetry install --no-root
```

### 3. Настройте переменные окружения

Создайте файл `.env` (или скопируйте `.env.example`):

```env
POSTGRES_PASSWORD=your_password
POSTGRES_USER=your_user
POSTGRES_DB=your_db
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

### 4. Запустите приложение

```bash
poetry run python -m app.main
```

## 🐳 Запуск через Docker

### 1. Соберите и запустите контейнеры

```bash
docker compose up --build
```

### 2. Остановите контейнеры

```bash
docker compose down
```

### ⚙️ Использование Taskfile (опционально)

Удобная замена длинным командам:

```bash
task install
task run
```
