from fastapi import Depends, HTTPException,Request
from fastapi import status

from sqlalchemy.ext.asyncio import AsyncSession

from jose import JWTError,jwt

from decouple import config

from app.database import get_db

from app.users.models import Users
from app.users.hashing import Hasher
from app.users.dao import get_user_by_email


async def authenticate_user(email:str,password:str,db:AsyncSession):
    user = await get_user_by_email(email,db)
    if not user:
        return
    if not Hasher.verify_password(password,user.password):
        return 
    return user

async def get_token(request:Request):
    token = request.cookies.get('access_token')
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return token


async def get_current_user_from_token(
    token: str = Depends(get_token), db: AsyncSession = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )
    try:
        payload = jwt.decode(
            token, config('SECRET_KEY'), algorithms=[config('ALGORITHM')]
        )
        email: str = payload.get("email")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = await get_user_by_email(email=email, db=db)
    if user is None:
        raise credentials_exception
    return user

async def get_current_admin(current_user:Users = Depends(get_current_user_from_token)):
    if current_user.role != 'admin':
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    return current_user