from fastapi import HTTPException,status

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.products.dao import set_model_column_new_value_by_id
from app.orders.models import Order
from app.orders.schemas import SOrderBase

from app.users.models import Users
from app.users.schemas import SUserCreate,SUserCreateResponse, SUserGet


from .hashing import Hasher


async def create_user(user: SUserCreate,db:AsyncSession):
    async with db:
        db_user = Users(first_name = user.first_name,last_name = user.last_name,email = user.email,password = Hasher.get_password_hash(user.password),role = 'user')
        db.add(db_user)
        await db.commit()
        await db.refresh(db_user)
        return SUserCreateResponse(id = db_user.id)


async def update_user(user:SUserCreate,new_data,db):
    res = await set_model_column_new_value_by_id(user.id,Users,new_data,db)
    return SUserGet(**res.__dict__)


async def get_user_by_email(email:str,db:AsyncSession):
    async with db:
        query = select(Users).where(Users.email == email)
        res = await db.execute(query)
        user_row = res.fetchone()
        if user_row is not None:
            return user_row[0]
        

async def update_order_status_by_id(id:int,new_status:str,db:AsyncSession):
    async with db:
        query = (update(Order).
        where(Order.id == id).
        values({'status':new_status}).
        returning(Order))
        res = await db.execute(query)
        await db.commit()
        order_row = res.fetchone()
        if order_row is not None:
            return SOrderBase(**order_row[0].__dict__)
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND)


    