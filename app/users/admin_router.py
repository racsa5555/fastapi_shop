from typing import List

from fastapi import APIRouter,Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.category.dao import create_category
from app.category.schemas import SCategoryCreate
from app.orders.schemas import SOrderBase
from app.products.models import Products
from app.products.schemas import SProduct, SProductCreate,SProductUpdate
from app.products.dao import create_product,get_products_by_ids,set_model_column_new_value_by_id

from app.users.dao import update_order_status_by_id
from app.users.login import get_current_admin
from app.users.schemas import SUserGet,SUpdateOrderStatus



router = APIRouter()

@router.patch('/order/update_order',response_model = SOrderBase)
async def update_status_order(order:SUpdateOrderStatus,admin:SUserGet = Depends(get_current_admin),db:AsyncSession = Depends(get_db)):
    return await update_order_status_by_id(order.id,order.status,db)

@router.post('/product',response_model = SProductCreate)
async def post_product(product:SProductCreate,db:AsyncSession = Depends(get_db),admin:SUserGet = Depends(get_current_admin)):
    res = await create_product(product,db)
    return SProductCreate.model_validate(res,from_attributes=True)

@router.patch('/product/update_product')
async def post_update_product(product:SProductUpdate,db:AsyncSession = Depends(get_db),admin:SUserGet = Depends(get_current_admin)):
    return await set_model_column_new_value_by_id(product.id,Products,product.model_dump(),db)

@router.post('/category')
async def post_category(category:SCategoryCreate,db:AsyncSession= Depends(get_db),admin:SUserGet = Depends(get_current_admin)):
    cat_id = await create_category(category,db)
    return {'id':cat_id}