from pydantic import BaseModel


class SUserCreate(BaseModel):
    first_name:str
    last_name:str
    email:str
    password: str

class SUserUpdate(BaseModel):
    first_name:str
    last_name:str

class SUserCreateResponse(BaseModel):
    id:int

class SUserLogin(BaseModel):
    email: str
    password: str

class SUserGet(BaseModel):
    first_name:str
    last_name:str
    email:str


class SUpdateOrderStatus(BaseModel):
    id:int
    status:str