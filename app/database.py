from sqlalchemy.ext.asyncio import AsyncSession,create_async_engine
from sqlalchemy.orm import DeclarativeBase,sessionmaker

from decouple import config


DB_PORT = config('DB_PORT')
DB_HOST = config('DB_HOST')
DB_NAME = config('DB_NAME')
DB_USER = config('DB_USER')
DB_PASS = config('DB_PASS')



DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_async_engine(
    DATABASE_URL
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