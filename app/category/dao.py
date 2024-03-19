from sqlalchemy.ext.asyncio import AsyncSession

from app.category.models import Category
from app.category.schemas import SCategoryCreate

async def create_category(category:SCategoryCreate,db:AsyncSession):
    async with db as session:
        category = Category(**category.model_dump())
        session.add(category)
        await session.commit()
        await session.refresh(category)
        return category.id
