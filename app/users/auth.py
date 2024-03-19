from datetime import timedelta

from fastapi import APIRouter, Depends,Response
from fastapi import HTTPException,status

from decouple import config

from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from security import create_access_token

from app.users.schemas import SUserCreate,SUserCreateResponse, SUserGet,SUserLogin
from app.users.dao import create_user,get_user_by_email
from app.users.login import authenticate_user, get_current_user_from_token


router = APIRouter()


@router.post('/auth/register',response_model = SUserCreateResponse)
async def register_user(user:SUserCreate,db:AsyncSession = Depends(get_db)):
    return await create_user(user,db)

@router.post('/auth/login')
async def login(response:Response,user_data: SUserLogin,db:AsyncSession = Depends(get_db)):
    user = await authenticate_user(user_data.email,user_data.password,db)
    if not user:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED)
    access_token_expires = timedelta(minutes=int(config('ACCESS_TOKEN_EXPIRE_MINUTES')))
    access_token = await create_access_token(
        data={"email": user.email},
        expires_delta=access_token_expires,
    )
    response.set_cookie('access_token',access_token,httponly=True)
    return {'detail': 'Вы успешно вошли в систему'}


@router.post('/auth/logout')
async def logout_user(response:Response):
    response.delete_cookie('access_token')
    return {'detail':'successfully'}
