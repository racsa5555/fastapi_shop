from typing import List

from fastapi import HTTPException,status

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from sqlalchemy import update

from app.products.models import Products
from app.products.schemas import SProductCreate,SProduct

async def create_product(product:SProductCreate,db:AsyncSession):
    async with db:
        db_product = Products(**product.model_dump())
        db.add(db_product)
        await db.commit()
        await db.refresh(db_product)
        return db_product

async def get_product_by_id(id:int,db:AsyncSession):
    query = select(Products).filter_by(id = id).options(joinedload(Products.category))
    result = await db.execute(query)
    product = result.scalar()
    if not product:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND)
    return product


async def check_and_set_quantity_product(products:List,quantitys:List,db:AsyncSession):
    print(quantitys)
    products_copy = products[:]
    quantitys_copy = quantitys[:]
    for index,product in enumerate(products_copy):
        if product.quantity < quantitys_copy[index]:
            raise HTTPException(detail=f'Продукт {products_copy.title} закончился на складе',status_code= status.HTTP_404_NOT_FOUND)
    for index,product in enumerate(products_copy):
        new_quantity = product.quantity-quantitys_copy[index]
        # new_quantity = products_copy.quantity - (quantitys_copy[index] if quantitys_copy[index] is not None else 1)
        await set_model_column_new_value_by_id(product.id,Products,{'quantity':new_quantity},db)
    return True




async def get_products(db:AsyncSession,title:str = None,category_id:int = None):
    query = select(Products)
    if title is not None:
        query = query.filter(Products.title == title)
    if category_id is not None:
        query = query.filter(Products.category_id == category_id)
    query = query.options(joinedload(Products.category))
    result = await db.execute(query)
    products = result.scalars().all()
    return [SProduct.model_validate(row,from_attributes=True) for row in products]

async def   get_products_by_ids(ids:List[int],db:AsyncSession):
    res = []
    for id in ids:
        res.append(await get_product_by_id(id,db))
    return res


async def set_model_column_new_value_by_id(id,cls,kwargs,db):
    async with db:
        query = (update(cls).
        where(cls.id == id).
        values(kwargs).
        returning(cls))
        res = await db.execute(query)
        await db.commit()
        res_row = res.fetchone()
        if res_row is not None:
            return res_row[0]
        return False


