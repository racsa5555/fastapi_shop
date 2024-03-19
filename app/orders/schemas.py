from typing import List, Optional

from pydantic import BaseModel



class SOrderItemCreate(BaseModel):
    product:int
    quantity:Optional[int] = 1

    class Config:
        from_attributes = True

class SOrderCreate(BaseModel):
    orders: List[SOrderItemCreate]
    address:str


    class Config:
        from_attributes = True

class SOrderGet(BaseModel):
    id:int
    totalsum:Optional[int]
    status: str
    address: str
    items:List[SOrderItemCreate]

    class Config:
        from_attributes = True

class SOrdersGet(BaseModel):
    
    orders: List[SOrderGet]

    class Config:
        from_attributes = True

class SOrderBase(BaseModel):
    id:int
    totalsum:Optional[int]
    status:str
    owner_id:int
    address:str