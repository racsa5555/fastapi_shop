from typing import Dict, List, Optional

from pydantic import BaseModel

from app.category.schemas import SCategoryCreate


class SProduct(BaseModel):
    id:int
    title:str
    description:str
    price: int
    image_id:str
    quantity:int
    category_id:int
    category: SCategoryCreate


    class Config:
        from_attributes = True


class SProductCreate(BaseModel):
    title:str
    description:str
    price: int
    image_id:str
    quantity:int
    category_id:int
    status:str = 'in_stock'

    class Config:
        from_attributes = True

class SProductUpdate(BaseModel):
    id: int
    price: Optional[int]
    quantity: Optional[int]
    description:Optional[str]
    image_id:Optional[str]


class SGetProduct(BaseModel):
    title:str
    description:str
    price:int
    quantity:int
    status:str
    category: SCategoryCreate

    class Config:
        from_attributes = True

class SListProducts(BaseModel):
    products: List[SProduct]
