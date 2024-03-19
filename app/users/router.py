from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db

from app.users.schemas import  SUserGet, SUserUpdate
from app.users.login import get_current_user_from_token
from app.users.dao import update_user


router = APIRouter()

@router.get('/me',response_model = SUserGet)
async def read_users_me(user:SUserGet = Depends(get_current_user_from_token),db:AsyncSession = Depends(get_db)):
    return user

@router.patch('/update')
async def patch_user(new_data:SUserUpdate, user:SUserGet = Depends(get_current_user_from_token),db:AsyncSession = Depends(get_db)):
    return await update_user(user,new_data.model_dump(),db)

# @router.post('/reset_password')
# async def reset_password(email:str):
#     pass

