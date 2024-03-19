from fastapi import APIRouter,Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.users.login import get_current_user_from_token
from app.users.schemas import SUserGet

from app.orders.dao import create_order, get_orders_by_user,delete_order
from app.orders.schemas import SOrderCreate, SOrdersGet



router = APIRouter()


@router.post('/')
async def post_order(order:SOrderCreate,db:AsyncSession = Depends(get_db),user:SUserGet = Depends(get_current_user_from_token)):
    res = await create_order(order,db,user)
    return res

@router.get('/my_orders',response_model = SOrdersGet)
async def get_orders(user:SUserGet = Depends(get_current_user_from_token),db:AsyncSession = Depends(get_db)):
    res = await get_orders_by_user(user,db)
    return SOrdersGet(orders = res)

@router.delete('/{order_id}')
async def del_order(order_id:int,user:SUserGet = Depends(get_current_user_from_token),db:AsyncSession = Depends(get_db)):
    res = await delete_order(order_id,user,db)
    return res