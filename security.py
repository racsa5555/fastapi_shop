from datetime import datetime
from datetime import timedelta

from typing import Optional

from decouple import config

from jose import jwt




async def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, config('SECRET_KEY'), algorithm=config('ALGORITHM')
    )
    return encoded_jwt



