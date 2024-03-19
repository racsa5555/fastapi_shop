from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db

from app.products.schemas import SGetProduct, SListProducts
from app.products.dao import get_product_by_id,get_products


router = APIRouter()


@router.get('/',response_model = SListProducts)
async def read_products(title: str = None,category_id:int = None,db:AsyncSession = Depends(get_db)):
    products = await get_products(db,title,category_id)
    return SListProducts(products = products)

@router.get('/{product_id}')
async def retrieve_product(product_id: int,db:AsyncSession = Depends(get_db)):
    product = await get_product_by_id(product_id,db)
    return SGetProduct.model_validate(product,from_attributes = True)
