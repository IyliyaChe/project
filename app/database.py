from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.config import settings

# Создание движка
engine = create_async_engine(settings.DATABASE_URL)

# Создание генератора сессий (транзакций)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# Создание базового класса для всех таблиц для удобства миграции через alembic
class Base(DeclarativeBase):
    pass