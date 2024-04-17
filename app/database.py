from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import AsyncSession,create_async_engine
from sqlalchemy.orm import DeclarativeBase,sessionmaker

from app.config import settings


if settings.MODE == "TEST":
    DATABASE_URL = settings.get_test_database_url()
    DATABASE_PARAMS = {"poolclass":NullPool}
else:
    DATABASE_URL = settings.get_database_url()
    DATABASE_PARAMS = {}

engine = create_async_engine(
    DATABASE_URL,**DATABASE_PARAMS
)
async_session_maker = sessionmaker(expire_on_commit=False,class_=AsyncSession,bind=engine)


async def get_db():
    try:
        session: AsyncSession = async_session_maker()
        yield session
    finally:
        await session.close()


class Base(DeclarativeBase):
    pass