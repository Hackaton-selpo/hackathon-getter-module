from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    # Настройки PostgreSQL
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    @property
    def POSTGRES_URL(self) -> str:
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    # Конфигурация загрузки переменных окружения
    model_config = ConfigDict(env_file=".env")  # type: ignore
    _ = model_config  # type: ignore


# Единственный экземпляр конфигурации, используемый в приложении
config: Config = Config()  # type: ignore[call-arg]
