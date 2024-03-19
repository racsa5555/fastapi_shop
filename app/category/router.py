from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.users.schemas import SUserGet
from app.users.login import get_current_admin

from .schemas import SCategoryCreate
from .dao import create_category

router = APIRouter()



