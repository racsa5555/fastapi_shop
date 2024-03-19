from fastapi import FastAPI
import uvicorn
from app.users.router import router as router_user
from app.category.router import router as router_category
from app.products.router import router as router_product
from app.orders.router import router as router_order
from app.users.admin_router import router as router_admin
from app.users.auth import router as router_auth
app = FastAPI()

app.include_router(router_auth,tags = ['auth'])
app.include_router(router_user,tags = ['users'],prefix = '/users')
app.include_router(router_category, prefix="/category", tags=["category"])
app.include_router(router_product, prefix="/product", tags=["product"])
app.include_router(router_order, prefix="/order", tags=["order"])
app.include_router(router_admin, prefix="/admin", tags=["admin"])



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)