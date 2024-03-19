from fastapi import HTTPException
from fastapi import status

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload


from app.products.dao import get_product_by_id, get_products_by_ids,check_and_set_quantity_product
from app.products.dao import set_model_column_new_value_by_id
from app.users.schemas import SUserGet

from app.orders.models import Order,OrderItem
from app.orders.schemas import SOrderCreate,SOrderGet

async def create_order(order:SOrderCreate,db:AsyncSession,user:SUserGet):
    try:
        async with db:
            db_order = Order(owner_id=user.id, address=order.address)
            items = order.orders
            products = await get_products_by_ids([item.product for item in items], db)
            quantitys = [item.quantity for item in items]
            await check_and_set_quantity_product(products, quantitys, db)
            db.add(db_order)
            await db.commit()
            await db.refresh(db_order)
            order_price = 0
            for item in items:
                db.add(OrderItem(product=item.product, quantity=item.quantity, order_id=db_order.id))
                product = await get_product_by_id(item.product, db)
                order_price += product.price * item.quantity
            await set_model_column_new_value_by_id(db_order.id, Order, {'totalsum': order_price}, db)
            await db.commit()
            return db_order
    except HTTPException as exc:
        return exc


async def get_order_by_id(id:int,db:AsyncSession):
    async with db:
        query = select(Order).where(Order.id == id)
        res = await db.execute(query)
        order_row = res.fetchone()
        if order_row is not None:
            return order_row[0]
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


async def get_orders_by_user(user:SUserGet,db:AsyncSession):
    async with db:
        query = (
        select(Order).filter(Order.owner_id == user.id)
        .options(joinedload(Order.items))
        )
        res = await db.execute(query)
        result_orm = res.unique().scalars().all()
        result_dto = [SOrderGet.model_validate(row, from_attributes=True) for row in result_orm]
        return result_dto
  

async def delete_order(order_id:int,user:SUserGet,db:AsyncSession):
    async with db:
        query = select(Order).filter_by(id = order_id)
        res = await db.execute(query)
        res = res.scalar()
        if res is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        if res.owner_id != user.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
        await db.delete(res)
        await db.commit()
        return order_id
    





