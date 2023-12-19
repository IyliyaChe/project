from pydantic.v1 import BaseSettings, root_validator

# Создается класс для конфигурации с помощью pydantic
class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str 

    # Создание переменной через валидатор
    @root_validator
    def get_database_url(cls, v):
        v["DATABASE_URL"] = f"postgresql+asyncpg://{v['DB_USER']}:{v['DB_PASS']}@{v['DB_HOST']}:{v['DB_PORT']}/{v['DB_NAME']}"
        return v
    
    class Config:
        env_file = ".env"

settings = Settings()

print(settings.DATABASE_URL)