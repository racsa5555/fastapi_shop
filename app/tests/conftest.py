import pytest

from app.database import Base,async_session_maker,engine
from app.config import settings
from app.users.models import Users
from app.category.models import Category
from app.orders.models import Order,OrderItem
from app.products.models import Products

@pytest.fixture(autouse=True)
async def prepare_database():
    assert settings.MODE == "TEST"

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    